import sublime, sublime_plugin
import datetime, getpass, time

class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  time.strftime("%Y-%m-%dT%H:%M:%S%z", time.gmtime()) } )

class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "%s" %  time.strftime("%H:%M:%S", time.gmtime()) } )
