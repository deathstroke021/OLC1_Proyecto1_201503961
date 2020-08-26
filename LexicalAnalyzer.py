import re


class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ('COMENTARIO', r'\/\/(.)*'),
            ('COMENTARIO_MULTILINEA', r'\/\*((.)*\n(.)*)+\*\/'),
            ('VAR', r'var'), 
            ('TRUE', r'true'), 
            ('FALSE', r'false'),
            ('IF', r'if'),
            ('CONSOLE', r'console'),
            ('LOG', r'log'),
            ('ELSE', r'else'),
            ('FOR', r'for'),
            ('WHILE', r'while'),
            ('DO', r'do'),
            ('CONTINUE', r'continue'),
            ('BREAK', r'break'),
            ('RETURN', r'return'),
            ('FUNCTION', r'function'),  
            ('CONSTRUCTOR', r'constructor'),
            ('THIS', r'this'), 
            ('MATH', r'math'),    
            ('POW', r'pow'),               
            ('ID', r'[a-zA-Z]\w*'),             
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER_CONST', r'\d(\d)*'),    
            ('CADENA', r'\"(.)*\"'),
            ('CARACTER', r'\'[a-zA-Z]\''),
            ('IGUAL', r'='),              
            ('ASTERICO', r'\*'),
            ('PUNTO_COMA', r';'),
            ('PARENTESIS_IZQ', r'\('),
            ('PARENTESIS_DER', r'\)'),
            ('MENOR_QUE', r'<'),              
            ('MAS_QUE', r'>'),
            ('PUNTO', r'\.'),
            ('LLAVE_IZQ', r'\{'),
            ('LLAVE_DER', r'\}'), 
            ('MÁS', r'\+'),
            ('AND', r'&'),
            ('DIAGONAL', r'\/'),
            ('GUION', r'-'),
            ('DOS_PUNTOS', r':'),
            ('COMA', r','),
            ('NEGACION', r'!'), 
            ('OR', r'\|'),   
            ('NEWLINE', r'\n'),         # NEW LINE
            ('SKIP', r'[ \t]+'),        # SPACE and TABS
            ('MISMATCH', r'.'),         # ANOTHER CHARACTER
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        # Lists of output for the program
        token = []
        lexeme = []
        row = []
        column = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                lin_start = m.end()
                self.lin_num += 1
            elif token_type == 'SKIP':
                continue
            elif token_type == 'MISMATCH':
                #raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
                #print('Error lexico')
                print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
            else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    if token_type == 'VAR' or token_type == 'TRUE' or token_type == 'FALSE' or token_type == 'IF'or token_type == 'CONSOLE' or token_type == 'LOG'or token_type == 'ELSE'or token_type == 'FOR'or token_type == 'WHILE'or token_type == 'DO'or token_type == 'CONTINUE'or token_type == 'BREAK'or token_type == 'RETURN'or token_type == 'FUNCTION'or token_type == 'CONSTRUCTOR'or token_type == 'THIS'or token_type == 'MATH'or token_type == 'POW':
                        #print('Palabra Reservada')
                        print('Token = PALABRA_RESERVADA, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                    else:
                        print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        
        return token, lexeme, row, column

