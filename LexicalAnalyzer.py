import re


class LexicalAnalyzer:
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
        error = []
        rowerror = []
        colerror = []

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
                        print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                        error.append(token_lexeme)
                        rowerror.append(self.lin_num)
                        colerror.append(col)
                    else:
                        token.append(token_type)
                        lexeme.append(token_lexeme)
                        row.append(self.lin_num)
                        # To print information about a Token
                        if token_type == 'ID':
                            if token_lexeme == 'var' or token_lexeme == 'true' or token_lexeme == 'false' or token_lexeme == 'if' or token_lexeme == 'console' or token_lexeme == 'log' or token_lexeme == 'else' or token_lexeme == 'for' or token_lexeme == 'while' or token_lexeme == 'do' or token_lexeme == 'continue' or token_lexeme == 'break' or token_lexeme == 'return' or token_lexeme == 'function' or token_lexeme == 'constructor' or token_lexeme == 'this' or token_lexeme == 'math' or token_lexeme == 'pow':
                                #print('Palabra Reservada')
                                print('Token = PALABRA_RESERVADA, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                            else:
                                print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))      
                        
                        else:
                            print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        
        return token, lexeme, row, column, error, rowerror, colerror
    
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
        error = []
        rowerror = []
        colerror = []

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
                    print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                    error.append(token_lexeme)
                    rowerror.append(self.lin_num)
                    colerror.append(col)
                
                else:
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    if token_type == 'ID':
                        if token_lexeme.lower() == 'color' or token_lexeme.lower() == 'border-style' or token_lexeme.lower() == 'border' or token_lexeme.lower() == 'text-allign' or token_lexeme.lower() == 'font-weight' or token_lexeme.lower() == 'padding-left' or token_lexeme.lower() == 'padding-top' or token_lexeme.lower() == 'line-height' or token_lexeme.lower() == 'margin-top' or token_lexeme.lower() == 'margin-left' or token_lexeme.lower() == 'display' or token_lexeme.lower() == 'top' or token_lexeme.lower() == 'float' or token_lexeme.lower() == 'min-width' or token_lexeme.lower() == 'background-color' or token_lexeme.lower() == 'opacity' or token_lexeme.lower() == 'font-family' or token_lexeme.lower() == 'font-size' or token_lexeme.lower() == 'padding-right' or token_lexeme.lower() == 'width' or token_lexeme.lower() == 'margin-right' or token_lexeme.lower() == 'position' or token_lexeme.lower() == 'right' or token_lexeme.lower() == 'clear' or token_lexeme.lower() == 'max-height' or token_lexeme.lower() == 'background-image' or token_lexeme.lower() == 'background' or token_lexeme.lower() == 'font-style' or token_lexeme.lower() == 'font' or token_lexeme.lower() == 'padding-bottom' or token_lexeme.lower() == 'padding' or token_lexeme.lower() == 'display' or token_lexeme.lower() == 'height' or token_lexeme.lower() == 'margin-bottom' or token_lexeme.lower() == 'margin' or token_lexeme.lower() == 'bottom' or token_lexeme.lower() == 'left' or token_lexeme.lower() == 'max-width' or token_lexeme.lower() == 'min-height' or token_lexeme.lower() == 'rgba' or token_lexeme.lower() == 'url' or token_lexeme.lower() == 'px' or token_lexeme.lower() == 'em' or token_lexeme.lower() == 'vh' or token_lexeme.lower() == 'vw' or token_lexeme.lower() == 'in' or token_lexeme.lower() == 'cm' or token_lexeme.lower() == 'mm' or token_lexeme.lower() == 'pt' or token_lexeme.lower() == 'pc' or token_lexeme.lower() == 'rem':
                            #print('Palabra Reservada')
                            print('Token = PALABRA_RESERVADA, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                        else:
                            print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))
                        
                    else:
                        print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))
 
        
        return token, lexeme, row, column, error, rowerror, colerror

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
        tokenerror = []
        lexemeerror = []

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
                    tokenerror.append(token_type)
                    lexemeerror.append(token_lexeme)
                    # To print information about a Token
                    if token_type == 'ID':
                        if token_lexeme == 'html' or token_lexeme == 'head' or token_lexeme == 'title' or token_lexeme == 'body' or token_lexeme == 'h1' or token_lexeme == 'h2' or token_lexeme == 'h3' or token_lexeme == 'h4' or token_lexeme == 'h5' or token_lexeme == 'h6' or token_lexeme == 'p' or token_lexeme == 'br' or token_lexeme == 'img' or token_lexeme == 'src' or token_lexeme == 'a' or token_lexeme == 'href' or token_lexeme == 'ol' or token_lexeme == 'ul' or token_lexeme == 'li' or token_lexeme == 'style' or token_lexeme == 'table' or token_lexeme == 'th' or token_lexeme == 'tr' or token_lexeme == 'border' or token_lexeme == 'caption' or token_lexeme == 'td' or token_lexeme == 'colgroup' or token_lexeme == 'col' or token_lexeme == 'thead' or token_lexeme == 'tbody' or token_lexeme == 'tfoot':
                            #print('Palabra Reservada')
                            print('Token = PALABRA_RESERVADA, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                        else:
                            print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

                    else:
                        print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        
        return token, lexeme, row, column, tokenerror, lexemeerror

    def tokenizermt(self, code):
        rules = [
            ('ID', r'[a-zA-Z]\w*'),             
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),
            ('INTEGER_CONST', r'\d(\d)*'),    
            ('CADENA', r'\"[^"]*\"'),             
            ('ASTERICO', r'\*'),
            ('PARENTESIS_IZQ', r'\('),
            ('PARENTESIS_DER', r'\)'),
            ('PUNTO', r'\.'),
            ('MÁS', r'\+'),
            ('DIAGONAL', r'\/'),
            ('GUION', r'-'),          
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
                        token.append(token_type)
                        lexeme.append(token_lexeme)
                        print('Error Lexico, Lexeme = \'{0}\', Row = {1}, Column = {2}'.format(token_lexeme, self.lin_num, col))
                        
                    else:
                        token.append(token_type)
                        lexeme.append(token_lexeme)
                        row.append(self.lin_num)
                        # To print information about a Token
                        print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))

        
        return token, lexeme, row, column  

