class CliCommand : 
    def __init__(self, cli_command):
        self.cli_command = cli_command

    def find_command_and_arguments(self):
        indexs  = self.__find_quotation_in_command()
        if len(indexs) > 1 : 
            return self.__manage_commands_with_quotes(indexs)
        else : 
            args = self.cli_command.split(" ")
            if len(args) > 1 : 
                return args[0], [args[1]]
            else : 
                return self.cli_command, []

    def __manage_commands_with_quotes(self, indexs): 
        message_to_post = self.cli_command[indexs[0]+1:indexs[1]]
        cli_command_without_big_argument = self.cli_command.replace(message_to_post, "").replace("\"", "").strip()
        elements_cli_command = cli_command_without_big_argument.split(" ")
        args = [elements_cli_command[1], message_to_post]
        return elements_cli_command[0], args

    def __find_quotation_in_command(self) -> list[int] :
        indexs = []
        for index , caracter in enumerate(self.cli_command) : 
            if caracter == "\"": 
                indexs.append(index)
        return indexs