class SerializerByActionMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.action_serializer_map.get(self.action, self.serializer_class)