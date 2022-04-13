from django.shortcuts import redirect


class RedirectToIndex:
    def dispatch(self, request, *args, **kwargs):
        # диспатч се грижи за access-a към даденото view
        if request.user.is_authenticated:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)
