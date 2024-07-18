from Interfaz import Aplicacion

# 1. Las clases no tienen el atributo ID puesto que este se autoincrementa en la base de datos
# 2. Para editar, se debe poner el nuevo valor en los cuadros superiores, indicar el ID 
# donde se cambiará en el cuadro inferior y darle al botón
# 3. Para eliminar, se debe indicar el ID de la fila que se va a eliminar en el
# cuadro inferior y darle al botón
# 4. Cuando se elimina un desarollador, también se eliminan todos sus proyectos
# 5. La columna DEV_ID en los proyectos, está totalmente vínculada a la columna ID en los
# desarrolladores, esto no permitirá que ahí haya un valor que no este en la otra

ejecutar = Aplicacion()