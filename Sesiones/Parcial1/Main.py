from Hospital import Hospital
from Paciente import Paciente
from Medico import Medico
from Consulta import Consulta

paciente1 = Paciente(idP=1, nombreP="Juan", apellidoP="Perez", dniP="12345678", fechaNacimiento="1990-01-01", grupoSanguineo="A+", historiaMedica="...")
paciente2 = Paciente(idP=2, nombreP="Maria", apellidoP="Gomez", dniP="87654321", fechaNacimiento="1985-05-15", grupoSanguineo="B-", historiaMedica="...")
paciente3 = Paciente(idP=3, nombreP="Carlos", apellidoP="Rodriguez", dniP="98765432", fechaNacimiento="1988-11-30", grupoSanguineo="O+", historiaMedica="...")

hospital1 = Hospital(idH=1, nombreH="San Juan", direccion="Calle 123", telefono="555-1234", especialidades=["Cardiología", "Neurología"], director="Dr. Smith", capacidad=200)
hospital2 = Hospital(idH=2, nombreH="San Roque", direccion="Avenida 456", telefono="555-5678", especialidades=["Pediatría", "Cirugía"], director="Dr. Johnson", capacidad=150)

medico1 = Medico(idM=1, nombreM="Dr. Smith", apellidoM="Johnson", dniM="12345678", especialidad="Cardiología", matricula="M123", aniosExperiencia=10)
medico2 = Medico(idM=2, nombreM="Dr. Rodriguez", apellidoM="Gomez", dniM="87654321", especialidad="Pediatría", matricula="M456", aniosExperiencia=8)
medico3 = Medico(idM=3, nombreM="Dra. Garcia", apellidoM="Perez", dniM="98765432", especialidad="Dermatología", matricula="M789", aniosExperiencia=12)

consulta1 = Consulta(idC=1, fecha="2023-01-15",paciente=paciente1,hospital=hospital1,diagnostico="Fiebre")
consulta2 = Consulta(idC=2, fecha="2023-02-20", paciente=paciente2,hospital=hospital2,diagnostico="Gripe")
consulta3 = Consulta(idC=3, fecha="2023-03-25", paciente=paciente3,hospital=hospital1,diagnostico="Dolor de cabeza")

paciente1.addDBPacientes()
paciente2.addDBPacientes()
paciente3.addDBPacientes()

hospital1.addDBHospitales()
hospital2.addDBHospitales()

medico1.addDBMedicos()
medico2.addDBMedicos()
medico3.addDBMedicos()

consulta1.addDBConsultas()
consulta2.addDBConsultas()
consulta3.addDBConsultas()