class GlobalPinMixin:
    def get_or_update_global_pin(self, global_pin=None):
        obj, created = self.get_or_create(pk=1)
        if global_pin:
            obj.global_pin = global_pin
            obj.save()
        return obj.global_pin
