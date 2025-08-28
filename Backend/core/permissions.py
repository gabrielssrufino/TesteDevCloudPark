from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        if not model_permission_codename:
            if hasattr(view, 'permission_codename'):
                return request.user.has_perm(view.permission_codename)
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        model = None
        app_label = None
        model_name = None

        try:
            if hasattr(view, 'model_class'):
                model = view.model_class
            elif hasattr(view, 'queryset') and view.queryset is not None:
                model = view.queryset.model
            elif hasattr(view, 'get_serializer'):
                serializer = view.get_serializer_class()
                if hasattr(serializer, 'Meta') and hasattr(serializer.Meta, 'model'):
                    model = serializer.Meta.model
            elif hasattr(view, 'model'):
                model = view.model

            if model:
                model_name = model._meta.model_name
                app_label = model._meta.app_label
                action = self.__get_action_sufix(method)
                return f'{app_label}.{action}_{model_name}'

            return None
        except (AttributeError, TypeError):
            return None

    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')