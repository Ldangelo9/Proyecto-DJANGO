from proyectopaq.mi_modulo import Cliente

def main():
    cliente1 = Cliente("Paul", "McCartney", 44, 1)
    print(cliente1)
    cliente1.mostrar_info()
    cliente1.servicio_pago()

main()