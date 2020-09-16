import re


class LexicalAnalyzercolor:
    # Token row
    lin_num = 1

    def tokenizejs(self, code):
        rules = [
            #('PRUEBA', r'[^5]'),
            ('COMENTARIO', r'\/\/(.)*'),
            ('COMENTARIO_MULTILINEA', r'\/(\*)+(.)*((.)*\n)*(\*)+\/'),
            #('COMENTARIO_MULTILINEA_UNILINEA', r'\/\*(.)*\*\/'),
            #('COMENTARIO_MULTILINEA', r'\/\*((.)*\n)*\*\/'),             
            ('ID', r'[a-zA-Z]\w*'),             
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER_CONST', r'\d(\d)*'),    
            ('CADENA', r'\"[^"]*\"'),
            ('CARACTER', r'\'[a-zA-Z]\''),
            ('CADENATIPO2', r'\'[^\']*\''), 
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
            #('ERROR', r'\^'),
            #('ERROR1', r'\%'),            
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
                token.append(token_type)
                lexeme.append(token_lexeme)
            elif token_type == 'SKIP':
                token.append(token_type)
                lexeme.append(token_lexeme)
                continue
            #elif token_type == 'MISMATCH':
                #raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
                #print('Error lexico')
                #print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
            else:
                    col = m.start() - lin_start
                    column.append(col)

                    if token_type == 'MISMATCH':
                        #print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                        token.append(token_type)
                        lexeme.append(token_lexeme)

                    else:
                        token.append(token_type)
                        lexeme.append(token_lexeme)
                        row.append(self.lin_num)
                        # To print information about a Token
                        
                        #print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        
        return token, lexeme, row, column
    
    def tokenizecss(self, code):
        rules = [
            ('COMENTARIO', r'\/\*(.)*\*\/'),
            ('COMENTARIO_MULTILINEA', r'\/\*((.)*\n+|([ \t]*\n)+)'),  
            #('COMENTARIO_MULTILINEA', r'\/(\*)+(.)*((.)*\n)*(\*)+\/'),
            #('COMENTARIO_MULTILINEA', r'\/\*((.)*\n(.)*)+\*\/'), 
            ('ID', r'[a-zA-Z]([a-zA-Z]|\d|-)*'),             
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER_CONST', r'\d(\d)*'),
            #('NEGATIVE_FLOAT_CONST', r'\-\d(\d)*\.\d(\d)*'),
            #('NEGATIVE_INTEGER_CONST', r'\-\d(\d)*'),
            ('SIGNO_MENOS', r'-'),    
            ('CADENA', r'\"(.)*\"'),
            ('LLAVE_IZQ', r'\{'),
            ('LLAVE_DER', r'\}'), 
            ('DOS_PUNTOS', r':'),
            ('PUNTO_COMA', r';'),
            ('ASTERICO', r'\*'),
            ('NUMERAL', r'\#'),
            ('COMA', r','),
            ('PUNTO', r'\.'),
            ('PORCENTAJE', r'\%'),
            ('PARENTESIS_IZQ', r'\('),
            ('PARENTESIS_DER', r'\)'),
            ('DIAGONAL', r'/'),  #
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
 
        #bitacoratoken = []
        #bitacoralexeme = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                lin_start = m.end()
                self.lin_num += 1
                token.append(token_type)
                lexeme.append(token_lexeme)
            elif token_type == 'SKIP':
                token.append(token_type)
                lexeme.append(token_lexeme)
                continue
            #elif token_type == 'MISMATCH':
                #raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
                #print('Error lexico')
                #print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
            else:
                col = m.start() - lin_start
                column.append(col)

                if token_type == 'MISMATCH':
                    #print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    #bitacoratoken.append(token_type)
                    #bitacoralexeme.append(token_lexeme)
                
                else:
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    #bitacoratoken.append(token_type)
                    #bitacoralexeme.append(token_lexeme)
                    # To print information about a Token
 
                    #print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))
 
        
        return token, lexeme, row, column

    def tokenizehtml(self, code):
        rules = [    
            ('COMENTARIO', r'<!--(.)*-->'),
            ('ID', r'[a-zA-Z]\w*'),              
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER_CONST', r'\d(\d)*'),
            #('NEGATIVE_FLOAT_CONST', r'\-\d(\d)*\.\d(\d)*'),
            #('NEGATIVE_INTEGER_CONST', r'\-\d(\d)*'),
            ('SIGNO_MENOS', r'-'),     
            ('CADENA', r'\"(.)*\"'),
            ('CADENA2', r'\'(.)*\''),
            ('MENOR_QUE', r'\<'),
            ('MAYOR_QUE', r'\>'),
            ('DIAGONAL', r'\/'),
            ('IGUAL', r'='),
            ('NEWLINE', r'\n'),         # NEW LINE
            ('SKIP', r'[ \t]+'),        # SPACE and TABS
            ('OTROS_SIMBOLOS', r'.'),         # ANOTHER CHARACTER
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
                token.append(token_type)
                lexeme.append(token_lexeme)
            elif token_type == 'SKIP':
                token.append(token_type)
                lexeme.append(token_lexeme)
                continue
            else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)

                    # To print information about a Token

                    #print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        
        return token, lexeme, row, column

    

