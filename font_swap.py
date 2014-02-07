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
    if font_prefs.get("font_a")["font_face"] == current_font:
      switch_to = font_prefs.get("font_a")
    else:
      switch_to = font_prefs.get("font_b")

    for (key, val) in switch_to:
      sublime_prefs.set(key, val)
