import logging
import os
import random

import openai
from django.core.management.base import BaseCommand
from records.models import AppConfig, Keypair
from twilio.rest import Client

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
)

# Alex's Twilio Account SID, Auth Token, and phone number
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_ID")
twilio_auth_token = os.getenv("TWILIO_TOKEN")
twilio_phone_number = os.getenv("TWILIO_NUMBER")

# Alex's OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Twilio Client
twilio_client = Client(twilio_account_sid, twilio_auth_token)


def generate_code():
    code = random.randint(1000, 9999)
    return str(code) + "#"


def generate_one_liner(code):
    prompt = (
        "Generate a funny one-liner text message for a secret Florida Panther themed bar. "  # noqa
        "The passcode for this month is {}.".format(code)
    )
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=60
    )
    one_liner = response.choices[0].text.strip()
    return one_liner.strip('"')


def generate_image():
    prompt = "A realistic painting of a light colored florida panther holding an alcoholic beverage playing hockey."  # noqa

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )

    # Return the URL of the image
    return response["data"][0]["url"]


def send_sms(phone_number, message, image_url):
    twilio_client.messages.create(
        body=message, from_=twilio_phone_number, media_url=[image_url], to=phone_number
    )


class Command(BaseCommand):
    help = "Generate new PIN for recipients and save them in pin.txt."

    def handle(self, *args, **kwargs):
        logging.info("Starting code generation.")

        new_code = generate_code()
        AppConfig.objects.get_or_update_global_pin(new_code)

        logging.info("Starting one-liner generation.")
        message = generate_one_liner(new_code)

        logging.info("Starting image generation.")
        image_url = generate_image()

        logging.info("Starting SMS sending.")
        for recipient in Keypair.objects.filter(is_active=True):
            send_sms(recipient.phone_number, message, image_url)

        logging.info("Completed successfully.")
