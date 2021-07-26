from errbot import BotPlugin, botcmd


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def teste(self, msg, args):  # a command callable with !tryme
        """
        ta dizendo que funciona.
        """
        return "It *works* !"  # This string format is markdown.
