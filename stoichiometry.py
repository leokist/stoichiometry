from math import pi, tan

class Reactants():
    def __init__(self, mols_c, mols_o, mols_h, mols_n):
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n

    def Composition(self):
        _composition = ""
        if self.mols_c != 0 :
            _composition += "C" + str(self.mols_c)
        if self.mols_h != 0 :
            _composition += "H" + str(self.mols_h)
        if self.mols_o != 0 :
            _composition += "O" + str(self.mols_o)
        if self.mols_n != 0 :
            _composition += "N" + str(self.mols_n)
        return _composition

class Products():
    """Cria um objeto Gás com suas propriedades"""
    def __init__(self, name, composition, massa_molar, mols_c, mols_o, mols_h, mols_n):
        self.name = name
        self.composition = composition
        self.massa_molar = massa_molar
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n
    
    def __repr__(self):
        return f"{self.composition}"
        

H2O = Products(
    name = "aguá",
    composition = "H2O",
    massa_molar = 18.01528,
    mols_c = 0,
    mols_o = 1,
    mols_h = 2,
    mols_n = 0
)

CO2 = Products(
    name = "",
    composition = "CO2",
    massa_molar = 44.00950,
    mols_c = 1,
    mols_o = 2,
    mols_h = 0,
    mols_n = 0
)
N2 = Products(
    name = "",
    composition = "N2",
    massa_molar = 28.0134,
    mols_c = 0,
    mols_o = 0,
    mols_h = 0,
    mols_n = 2
)


class Reaction():
    def __init__(self, fuel, oxidizer):
        self._comb = fuel
        self._oxid = oxidizer
    
    """
    #
    # Stoichiometric Reaction
    #
    """
    def Stoichiometry(self):
        """
        Perform the calculation of the stoichiometric reaction.
        """
        self._produtos_estequiometrico = []
        self._matriz_estequiometrica = []
        self._n_comb_estequiometrico = 1
        self._razao_equiv = 1
        self._propelentes = [self._comb, self._oxid]
        
        """
                b                      c             d                      a
        [self.oxid.mols_o, - prod1.mols_o, - prod2.mols_o, - self.comb.mols_o],
        [self.oxid.mols_h, - prod1.mols_h, - prod2.mols_h, - self.comb.mols_h],
        [self.oxid.mols_c, - prod1.mols_c, - prod2.mols_c, - self.comb.mols_c],
        """

        # Define os produtos de uma reação estequiométrica
        "a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2"
        if self._razao_equiv != 0 and (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
            self._produtos_estequiometrico.append([H2O, 0])
        if self._razao_equiv != 0 and (self._comb.mols_c > 0 or self._oxid.mols_c > 0) and (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
            self._produtos_estequiometrico.append([CO2, 0])
        if self._razao_equiv != 0 and (self._comb.mols_n > 0 or self._oxid.mols_n > 0):
            self._produtos_estequiometrico.append([N2, 0])
                
        # Obtém a quantidade total de produtos da reação
        n_produtos = len(self._produtos_estequiometrico)

        # Obtem a quantidade total de reagentes da reação
        n_propelentes = len(self._propelentes)

        # Obtém a quantidade total de elementos
        if self._comb.mols_o != 0 or self._oxid.mols_o != 0:
            n_elementos = 1
        if self._comb.mols_h != 0 or self._oxid.mols_h != 0:
            n_elementos += 1
        if self._comb.mols_c != 0 or self._oxid.mols_c != 0:
            n_elementos += 1
        if self._comb.mols_n != 0 or self._oxid.mols_n != 0:
            n_elementos += 1
                
        # Gera uma matriz de template com as linhas necessárias
        
        matriz = [] #self.matriz
        lin = 0
        while lin < n_elementos:
            matriz.append([])
            lin += 1

        # Adiciona o numero de mols de cada espécie na matriz
        n_especies = n_produtos + n_propelentes
        lin = 0
        col = 0
        contador = 0
        while lin < n_elementos:
            if contador == 0:
                if self._comb.mols_o == 0 and self._oxid.mols_o == 0:
                    lin = 0
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_o)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_o)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self._propelentes[0].mols_o)
                        col += 1
                    lin += 1
                    col = 0
            elif contador == 1:
                if self._comb.mols_h == 0 and self._oxid.mols_h == 0:
                    lin = 1
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_h)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_h)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self._propelentes[0].mols_h)
                        col += 1 
                    lin += 1
                    col = 0
            elif contador == 2:
                if self._comb.mols_c == 0 and self._oxid.mols_c == 0:
                    lin = 2
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_c)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_c)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self._propelentes[0].mols_c)
                        col += 1 
                    lin += 1
                    col = 0
            elif contador == 3:
                if self._comb.mols_n != 0 or self._oxid.mols_n != 0:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_n)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_n)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, - 1 * self._propelentes[0].mols_n)
                        col += 1
                    lin += 1
                    col = 0
            contador += 1

        """
        # Cálculo do numero de mol de cada produto e reagente
        # Cálculo efetuado pelo método de Eliminação de Gauss
        """
        # Zera os elementos abaixo da diagonal da matriz
        col = 0
        pivo_x = 0
        lin = pivo_x + 1
        while lin < n_elementos:
            if matriz[lin][col] == 0:
                lin += 1
            else:
                pivo = matriz[pivo_x][pivo_x]
                multp = matriz[lin][col] / pivo
                x = 0
                for i in matriz[lin]:                  
                    matriz[lin][x] = i - multp * matriz[pivo_x][x]
                    x += 1
                lin += 1
            if lin == len(matriz):
                pivo_x += 1
                lin = pivo_x + 1
                col += 1

        # Zera os elementos acima da diagonal da matriz
        pivo_x = n_elementos - 1
        col = pivo_x
        lin = pivo_x - 1
        while lin >= 0:
            if matriz[lin][col] == 0:
                lin -= 1
            else:
                pivo = matriz[pivo_x][pivo_x]
                multp = matriz[lin][col] / pivo
                x = 0
                for i in matriz[lin]:
                    matriz[lin][x] = i - multp * matriz[pivo_x][x]
                    x += 1
                lin -= 1
            if lin == -1:
                pivo_x -= 1
                col = pivo_x
                lin = pivo_x - 1
        
        # Obtem a solução
        pivo_x = 0
        lin = 0
        col = 0
        y = 0
        while lin < n_elementos:
            pivo = matriz[lin][col]
            x = 0
            for i in matriz[lin]:
                matriz[lin][x] = matriz[lin][x] / pivo
                x += 1
            lin += 1
            col += 1

        # Mapeamento dos resultados
        y = 0
        while y < len(matriz)-1:
            self._produtos_estequiometrico[y][1] = matriz[y+1][len(matriz)]
            y += 1
            lin += 1

        self._n_oxid = matriz[0][-1]
                                  

        
    
    @property
    def fullReaction(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        # Retorna o resultado da reação estequiométrica
        if self._razao_equiv == 1:
            reacao = f"{self._n_comb_estequiometrico} {self._propelentes[0].Composition()} + %.3f  {self._propelentes[1].Composition()} --> " %(self._n_oxid)

            x = 0
            for i in self._produtos_estequiometrico:

                reacao += f"%.3f {self._produtos_estequiometrico[x][0]}" %(self._produtos_estequiometrico[x][1])
                if i is not self._produtos_estequiometrico[-1]:
                    reacao += " + "
                x += 1

        return reacao
      

  