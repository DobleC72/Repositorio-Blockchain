#CESARCARRILLO --07/05/2023 *se creo la base del proyecto de blockchain*
import hashlib
import datetime

class Bloque:
    def __init__(self, numero_bloque, transacciones, hash_anterior):
        self.numero_bloque = numero_bloque
        self.transacciones = transacciones
        self.timestamp = datetime.datetime.now()
        self.hash_anterior = hash_anterior
        self.hash_actual = self.calcular_hash()

    def calcular_hash(self):
        datos = str(self.numero_bloque) + str(self.transacciones) + str(self.timestamp) + str(self.hash_anterior)
        hash = hashlib.sha256(datos.encode('utf-8')).hexdigest()
        return hash

class Blockchain:
    def __init__(self):
        self.bloques = [self.crear_bloque_genesis()]

    def crear_bloque_genesis(self):
        return Bloque(0, [], "0")

    def obtener_ultimo_bloque(self):
        return self.bloques[-1]

    def agregar_bloque(self, nuevo_bloque):
        nuevo_bloque.hash_anterior = self.obtener_ultimo_bloque().hash_actual
        nuevo_bloque.hash_actual = nuevo_bloque.calcular_hash()
        self.bloques.append(nuevo_bloque)

    def validar_cadena(self):
        for i in range(1, len(self.bloques)):
            bloque_actual = self.bloques[i]
            bloque_anterior = self.bloques[i-1]

            if bloque_actual.hash_actual != bloque_actual.calcular_hash():
                return False

            if bloque_actual.hash_anterior != bloque_anterior.hash_actual:
                return False

        return True

# Crear una instancia de la clase Blockchain
blockchain = Blockchain()

# Agregar un bloque de transacciones
transacciones_bloque_1 = ["transaccion_1", "transaccion_2", "transaccion_3"]
bloque_1 = Bloque(1, transacciones_bloque_1, "")
blockchain.agregar_bloque(bloque_1)

# Agregar otro bloque de transacciones
transacciones_bloque_2 = ["transaccion_4", "transaccion_5", "transaccion_6"]
bloque_2 = Bloque(2, transacciones_bloque_2, "")
blockchain.agregar_bloque(bloque_2)

# Agregar otro bloque de transacciones
transacciones_bloque_3 = ["transaccion_7", "transaccion_8", "transaccion_9"]
bloque_3 = Bloque(3, transacciones_bloque_3, "")
blockchain.agregar_bloque(bloque_3)

# Imprimir la cadena de bloques
for bloque in blockchain.bloques:
    print("Número de bloque: ", bloque.numero_bloque)
    print("Transacciones: ", bloque.transacciones)
    print("Timestamp: ", bloque.timestamp)
    print("Hash anterior: ", bloque.hash_anterior)
    print("Hash actual: ", bloque.hash_actual)
    print("------------------------")

# Validar la cadena
print("La cadena es válida:", blockchain.validar_cadena())

