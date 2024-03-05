## Hooks

### Example usage of registering a custom alert from code

We provide hooks to allow you to add your own alerts to the alerts list.
This is useful if you want to add alerts based on some condition in your code.

```python
@hooks.register('wagtail_alerts.construct_alerts')
def construct_alerts(request, base_list, settings):
    """
    Construct the alerts for the request.
    """
    ...
    if some_condition:
      alerts.append(Alert(
          title="This is a test alert",
          body="This is a test alert body",
          alert_type="primary",
          dismissible=True,
          duration=5000,
          alert_type="TOAST",
      ))

```

### Example of changing the alert styles

We provide hooks to let you change the styles of the alerts.
This is useful if you want to change the colors of the alerts based on your theme.

```python
from wagtail import hooks

@hooks.register("wagtail_alerts.construct_styles")
def construct_styles(request, styles, settings):
    styles.change_color("primary", "#ff0000")
    styles.change_theme("dark", "#000000")
    styles.PRIMARY.text_color = "#ff0000"
    styles.PRIMARY.theme_color = "rgba(0, 0, 0, 0.5)"
```
