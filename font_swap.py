import sublime
import sublime_plugin


class FontSwapCommand(sublime_plugin.ApplicationCommand):
  """
  Quickly swap font settings.
  """
  def run(self):
    sublime_prefs = sublime.load_settings("Preferences.sublime-settings")
    font_prefs = sublime.load_settings("FontSwap.sublime-settings")

    current_font = sublime_prefs.get("font_face")
    switch_to = "font_b" if font_prefs.get("font_a")["font_face"] == current_font else "font_a"

    print("switching font options to " + switch_to)
    switch_to = font_prefs.get(switch_to)

    for key, val in switch_to.items():
      sublime_prefs.set(key, val)
