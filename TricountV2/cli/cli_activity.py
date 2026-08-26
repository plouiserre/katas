from TricountV2.cli.CommandBadFormattingException import CommandBadFormattingException

class CliActivity : 
    def __init__(self, cli_command):
        self.cli_command = cli_command

    def decompose_arguments(self):
        arguments_between_brackets_with_brackets = self.__find_arguments_with_brackets()
        arguments_between_brackets_transformed = self.__transform_argument_between_bracket()
        self.cli_command = self.cli_command.replace(arguments_between_brackets_with_brackets, arguments_between_brackets_transformed)
        arguments = self.__split_arguments()
        return arguments
    
    def __find_arguments_with_brackets(self):
        indexs = self.__find_indexs_brackets()
        brackets_content_with_brackets = self.cli_command[indexs[0]:indexs[1]+1]
        return brackets_content_with_brackets
    
    def __transform_argument_between_bracket(self): 
        brackets_arguments = self.__find_arguments_between_brackets()
        brackets_arguments = ' '.join(brackets_arguments.split())
        brakets_arguments_glu = brackets_arguments.strip().replace(" ","_")
        return brakets_arguments_glu
    
    def __find_arguments_between_brackets(self):
        indexs = self.__find_indexs_brackets()
        brakets_arguments = self.cli_command[indexs[0]+1:indexs[1]]
        return brakets_arguments
    
    def __find_indexs_brackets(self):
        indexs_first_caracter = []
        indexs_second_caracter = []
        for index , caracter in enumerate(self.cli_command) : 
            if caracter == "[": 
                indexs_first_caracter.append(index)
        for index , caracter in enumerate(self.cli_command) : 
                    if caracter == "]": 
                        indexs_second_caracter.append(index)
        if len(indexs_first_caracter) != 1  or len(indexs_second_caracter) != 1: 
            raise CommandBadFormattingException("arguments are bad formatting")
        indexs = [indexs_first_caracter[0], indexs_second_caracter[0]]
        return indexs
    
    def __split_arguments(self):
        args = self.cli_command.split(" ")
        command = args[0]
        args.remove(args[0])
        arguments = []
        for arg in args :
            arguments.append(arg)
        return arguments