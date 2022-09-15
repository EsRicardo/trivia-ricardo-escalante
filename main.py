respuestas_correctas = 0
iniciar_trivia = True  
intentos = 0
while iniciar_trivia == True:
  intentos += 1
  puntaje = 0
  input ("\033[1;33m " +
      " _________♛▁▂▃▅ GRAN TRIVIA DE CULTURA GENERAL ▅▃▂▁♛_________" +
      '\033[0;m')
  print ()
  print ("\033[1;35m " +
    "Hola, mi nombre es Socrates, y vamos a comenzar una aventura juntos en la cual pondremos a prueba tus conocimientos sobre temas generales."
    + '\033[0;m')
  print ()
  import time
  NombreR = str(input("Como deseas que te llame? "))
  print("Ohhhhhhhhh......")
  time.sleep(1)
  print("Me gusta tu nombre " + NombreR + " nos espera una gran aventura")
  print(
    "\033[32m Ok " + NombreR +
    " A continuacion, te pesentaremos una serie de preguntas de cultura general, como historia, matematicas, biologia lenguaje, etc."
)
  input()
  input(
    "Tendras que responder las preguntas escribiendo la letra de la alternativa que consideres correcta en MINUSCULA y presiona ENTER para enviar tu respuesta, la dificultad de las preguntas aumentara conforme avances de nivel, pero al final todo depende de tus conocimientos y cuanto te acuerdas de ellos, No te preocupes, es solo un juego."
)
  print(
    "Hay tres niveles, en el primero tendras 3 posibles respuestas de las cuales una sola es verdadera."
)
  input(
    " En los niveles 2 y 3 se agregarán una y dos alternativas mas respecto a la primera."
)
  print(
    "En el primer nivel, te daremos la respuesta a la pregunta ya sea si has respondido correctamente o no. Asimismo, si respondes de manera incorrecta las preguntas del segundo y tercer nivel, no tendras la respuesta, tendras que averiguarlo por ti mismo acabada la trivia y podras volver a intentarlo en el siguente turno."
)
  print("Buena suerte " + NombreR + " ¡¡¡Exitosツ!!!")
  input()
  print ("\033[4;35;47m" + "                    .                    " + '\033[0;m')
  print ("\033[4;35;47m" + "_____☆♚☆╬═══« NIVEL  UNO »═══╬☆♚☆_____   " + '\033[0;m')
  print ("\033[4;35;47m" + "                    .                    " + '\033[0;m')
  print ()
  print("1. ¿Cual fue el creador del famoso detective ingles Sherlock Holmes?")
  print()
  print("a) Edgar Allan Poe")
  print("b) Arthur Conan Doyle.")
  print("c) Jorge Luis Borges")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  while respuesta_usuario not in ("a", "b", "c"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
   respuesta_correcta = "b"
   if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! Sherlock Holmes fue creado por Arthur Conan Doyle haciendo aparicion en el libro Estudio en escarlata publicado en 1887"
    )
    respuestas_correctas = respuestas_correctas + 1
   elif respuesta_usuario == "a":
     print(
        "¡Incorrecto! Sherlock Holmes fue creado por Arthur Conan Doyle haciendo aparicion en el libro Estudio en escarlata publicado en 1887"
    )
   elif respuesta_usuario == "b":
    print(
        "¡Correcto! Sherlock Holmes fue creado por Arthur Conan Doyle haciendo aparicion en el libro Estudio en escarlata publicado en 1887"
    )
   elif respuesta_usuario == "c":
     print(
        "¡Incorrecto! Sherlock Holmes fue creado por Arthur Conan Doyle haciendo aparicion en el libro Estudio en escarlata publicado en 1887"
    )
  print ()
  print("2. ¿Quien invento la dinamita?")
  print()
  print("a) Alfred Nobel")
  print("b) Thomas Alva Edison.")
  print("c) Alexander Graham Bell")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "a"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! Alfred Nobel invento la dinamita y la patento en 1867, una curiosidad es que, al sentir culpa por las muertes que habia causado su invento, decidio con su fortuna crear la famosa fundacion Nobel, encargada de premiar a las personas e instituciones que favorecieron a la Humanidad en los diversos campos de estudio."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Correcto! Alfred Nobel invento la dinamita y la patento en 1867, una curiosidad es que, al sentir culpa por las muertes que habia causado su invento, decidio con su fortuna crear la famosa fundacion Nobel, encargada de premiar a las personas e instituciones que favorecieron a la Humanidad en los diversos campos de estudio."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Incorrecto! Alfred Nobel invento la dinamita y la patento en 1867, una curiosidad es que, al sentir culpa por las muertes que habia causado su invento, decidio con su fortuna crear la famosa fundacion Nobel, encargada de premiar a las personas e instituciones que favorecieron a la Humanidad en los diversos campos de estudio."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Incorrecto! Alfred Nobel invento la dinamita y la patento en 1867, una curiosidad es que, al sentir culpa por las muertes que habia causado su invento, decidio con su fortuna crear la famosa fundacion Nobel, encargada de premiar a las personas e instituciones que favorecieron a la Humanidad en los diversos campos de estudio."
    )
  print()
  print("3. ¿Qué expresa esta formula: e = mc²?")
  print()
  print("a) La Teoria de la Probabilidad")
  print("b) Volumen de un prisma rectangular ")
  print("c) Equivalencia entre masa y energia")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
   respuesta_correcta = "c"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! e = mc² representa una equivalencia entre la masa y la energía, esta se establece por la expresión de la teoría de la relatividad."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto! e = mc² representa una equivalencia entre la masa y la energía, esta se establece por la expresión de la teoría de la relatividad."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Incorrecto! e = mc² representa una equivalencia entre la masa y la energía, esta se establece por la expresión de la teoría de la relatividad."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Correcto! e = mc² representa una equivalencia entre la masa y la energía, esta se establece por la expresión de la teoría de la relatividad."
    )
  print ()
  print("4. ¿Quien fue coronado Rey de Francia el dia 25/09/2020?")
  print()
  print("a) Luis XI")
  print("b) Pedro XIX")
  print("c) No fue coronado ningun Rey Frances ese dia")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c"):
    respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "c"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! En Francia dejo de existir la monarquia desde el 21 de septiembre de 1792, cuando la Asamblea legislativa proclamó la abolición de la monarquía, dando paso a la Primera República francesa."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto! En Francia dejo de existir la monarquia desde el 21 de septiembre de 1792, cuando la Asamblea legislativa proclamó la abolición de la monarquía, dando paso a la Primera República francesa."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Incorrecto! En Francia dejo de existir la monarquia desde el 21 de septiembre de 1792, cuando la Asamblea legislativa proclamó la abolición de la monarquía, dando paso a la Primera República francesa."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Correcto! En Francia dejo de existir la monarquia desde el 21 de septiembre de 1792, cuando la Asamblea legislativa proclamó la abolición de la monarquía, dando paso a la Primera República francesa."
    )
  print()
  print("5. ¿Quién fue Gregor Mendel?")
  print()
  print(
    "a) Fue un monje y naturalista que es considerado el padre de la genética "
)
  print(
    "b) Fue un oficial y medico aleman en la SGM conocido por sus terribles experimentos"
)
  print(
    "c) Fue un científico francés cuyos descubrimientos tuvieron una gran importancia en diversos campos de las ciencias naturales, especialmente en la química y en la microbiología."
)
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "a"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! Gregor Johann Mendel fue un fraile agustino católico y naturalista. Formuló, por medio de los trabajos que llevó a cabo con diversa variedad de guisantes y arvejas, las hoy llamadas leyes de Mendel que dieron origen a la herencia genética."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Correcto! Gregor Johann Mendel fue un fraile agustino católico y naturalista. Formuló, por medio de los trabajos que llevó a cabo con diversa variedad de guisantes y arvejas, las hoy llamadas leyes de Mendel que dieron origen a la herencia genética."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Incorrecto! Gregor Johann Mendel fue un fraile agustino católico y naturalista. Formuló, por medio de los trabajos que llevó a cabo con diversa variedad de guisantes y arvejas, las hoy llamadas leyes de Mendel que dieron origen a la herencia genética."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Incorrecto! Gregor Johann Mendel fue un fraile agustino católico y naturalista. Formuló, por medio de los trabajos que llevó a cabo con diversa variedad de guisantes y arvejas, las hoy llamadas leyes de Mendel que dieron origen a la herencia genética."
    )
  print(
    "\033[1;35m " + " Aja " + NombreR +
    ", veo que estas respondiendo las preguntas. Yo, tu amigo Socrates te voy avisando que la pregunta siguiente es la JEFE del NIVEL UNO, si la respondes correctamente, tendras un bono de ¡¡¡3 PUNTOS!!! que se sumara a tu puntaje obtenido. VAMOS!!! TU PUEDES...!!!"
    + '\033[0;m')
  print()
  input()
  print("\033[4;31;41m" + "                     " + '\033[0;m')
  print("\033[4;31;41m" + "☠ ☠ ¡¡¡BOSS!!!☠ ☠    " + '\033[0;m')
  print ("\033[4;31;41m" + "                     " + '\033[0;m')
  print()
  print(
    "6. ¿Si X es menor que Y por una diferencia de 6 e Y es el doble de Z, ¿cuál es el valor de X cuando Z es igual a 2?"
)
  print()
  print("a) 12")
  print("b) -2")
  print("c) 4")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "b"
  if respuesta_usuario == respuesta_correcta:
    print("¡Correcto! Respuesta: -2")
    print("Explicación paso a paso:")
    print("Y - X = 6 ----- Y = 6+X")
    print("Y = 2 Z")
    print("6 + X = 2 Z  /   Cuando Z vale 2")
    print("6+X = 2*2")
    print("X= 4-6")
    print("X=-2")
    respuestas_correctas = respuestas_correctas + 3
  elif respuesta_usuario == "a":
    print("¡Incorrecto! Respuesta: -2")
    print("Explicación paso a paso:")
    print("Y - X = 6 ----- Y = 6+X")
    print("Y = 2 Z")
    print("6 + X = 2 Z  /   Cuando Z vale 2")
    print("6+X = 2*2")
    print("X= 4-6")
    print("X=-2")
  elif respuesta_usuario == "b":
    print("¡Correcto! Respuesta: -2")
    print("Explicación paso a paso:")
    print("Y - X = 6 ----- Y = 6+X")
    print("Y = 2 Z")
    print("6 + X = 2 Z  /   Cuando Z vale 2")
    print("6+X = 2*2")
    print("X= 4-6")
    print("X=-2")
  elif respuesta_usuario == "c":
    print("¡Incorrecto! Respuesta: -2")
    print("Explicación paso a paso:")
    print("Y - X = 6 ----- Y = 6+X")
    print("Y = 2 Z")
    print("6 + X = 2 Z  /   Cuando Z vale 2")
    print("6+X = 2*2")
    print("X= 4-6")
    print("X=-2")
  print()

  print ("\033[1;35m " + "Socrates:_Bueno " + NombreR +
    " Culminaste el NIVEL UNO, Felicidades, de a partir del siguiente Enter empezara el temido NIVEL DOS, tomate un descanso para empezar con energia el siguente nivel, exitos y buena suerte"
    + '\033[0;m')
  input ()
  print ("\033[4;34;43m" + "                                " + '\033[0;m')
  print ("\033[4;34;43m" + "_____㎜『 ㎝ NIVEL DOS ㎝』㎜_____" + '\033[0;m')
  print ("\033[4;34;43m" + "                                " + '\033[0;m')
  print()

  print("\n7. ¿Quien fue el dictador romano que fue asesinado en los idus de marzo del año 44 a. C.?")
  print("a) Marco Aurelio")
  print("b) Gayo Julio César")
  print("c) Cesar Augusto")
  print("d) Diocleciano")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c", "d"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "b"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! Gayo Julio Cesar, o solo Julio Cesar, fue el ultimo Dictador Romano, asesinado por algunos miembros del Senado, con su muerte, se marca el principio de lo que fue el Imperio Romano."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto! Marco Aurelio no goberno Roma en ningun momento de su vida."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Correcto! Gayo Julio Cesar, o solo Julio Cesar, fue el ultimo Dictador Romano, asesinado por algunos miembros del Senado, con su muerte, se marca el principio de lo que fue el Imperio Romano."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Incorrecto! Cesar Augusto fue el primer Emperador Romano."
    )
  elif respuesta_usuario == "d":
    print(
        "¡Incorrecto! Diocleciano fue el 48avo Emperador Romano."
    )
  print("\n8. ¿Cual es el primer atributo que se otorga la Iglesia Catolica?")
  print("a) Catolica")
  print("b) Santa")
  print("c) Una")
  print("d) Apostolica")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c", "d"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "c"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! La Iglesia Catolica se considera UNA debido a su origen, Dios mismo. Dios es uno según la doctrina católica, y tambien es una debido a su Fundador, Cristo."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto! CATOLICA es el tercer atributo de la Iglesia Catolica."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Incorrecto! SANTA, es el segundo atributo de la Iglesia Catolica."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Correcto! La Iglesia Catolica se considera UNA debido a su origen, Dios mismo. Dios es uno según la doctrina católica, y tambien es una debido a su Fundador, Cristo."
    )
  elif respuesta_usuario == "d":
    print(
        "¡Incorrecto! APOSTOLICA es el cuarto atributo de la Iglesia Catolica."
    )
  print("\n9. Identifique el termino, en minusculas, que mas se aleje del campo semantico al que remiten el enunciado en mayusculas y los restantes terminos en minusculas")
  print ("MEMORIA")
  print("a) añoranza")
  print("b) amnesia")
  print("c) remembranza")
  print("d) recuerdo")
  print()
  respuesta_usuario = input ("Escribe la letra de la respuesta en MINÚSCULA:")
  print()
  while respuesta_usuario not in ("a", "b", "c", "d"):
    respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
    respuesta_correcta = "b"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! Amnesia es el termino mas alejado de memoria."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto!"
    )
  elif respuesta_usuario == "b":
    print(
        "¡Correcto! Amnesia es el termino mas alejado de memoria."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Incorrecto!"
    )
  elif respuesta_usuario == "d":
    print(
        "¡Incorrecto!"
    )
  print("\n10. Filosofo que definio a la filosofia como ACTIVIDAD RACIONAL ESCLARECEDORA DEL LENGUAJE")
  print ()
  print("a) Santo Tomas de Aquino")
  print("b) Ludwing Wittgenstein")
  print("c) Inmanuel Kant")
  print("d) Friedrich Nietzsche")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  while respuesta_usuario not in ("a", "b", "c", "d"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "b"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! Para Wittgenstein la filosofía entendida al modo tradicional, entendida como una doctrina acerca de lo real, consta de sinsentidos. La única forma correcta de hacer filosofía es la de mostrar los límites del discurso con sentido, mostrar los límites de lo que puede ser conocido y expresado mediante el lenguaje."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto! Tomás de Aquino concibe la filosofia como la ciencia que considera el orden que la razón humana introduce en los actos de la voluntad."
    )
  elif respuesta_usuario == "b":
    print(
        "¡Correcto!  Para Wittgenstein la filosofía entendida al modo tradicional, entendida como una doctrina acerca de lo real, consta de sinsentidos. La única forma correcta de hacer filosofía es la de mostrar los límites del discurso con sentido, mostrar los límites de lo que puede ser conocido y expresado mediante el lenguaje."
    )
  elif respuesta_usuario == "c":
    print(
        "¡Incorrecto!La filosofía, según Kant, se distingue del conocimiento racional <<En que presenta en ciencia separada lo que la segunda sólo concibe como mezclado>>"
    )
  elif respuesta_usuario == "d":
    print(
        "¡Incorrecto! Segun Nietzsche, los principales fundamentos de la filosofía es la negación de que el ser humano es un ser racional. " 
    )
  print("\n11. La cultura Chimu se desarrollo en la _________ del Peru y su centro arquitectonico principal fue la ciudad de _________.")
  print("a) Costa Sur-Chan Chan")
  print("b) Sierra Sur-Caral")
  print("c) Sierra Norte-Kalasasaya")
  print("d) Costa Norte-Chan-Chan")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print()
  while respuesta_usuario not in ("a", "b", "c", "d"):
   respuesta_usuario = input("Debes responder a, b o c. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "d"
  if respuesta_usuario == respuesta_correcta:
    print(
        "¡Correcto! La cultura Chimú, o también llamado el reino de Chimor, surgió en la costa norte de Perú entre los siglos XII y XV de nuestra era. Con su capital en Chan Chan actual departamento de La Libertad."
    )
    respuestas_correctas = respuestas_correctas + 1
  elif respuesta_usuario == "a":
    print(
        "¡Incorrecto!"
    )
  elif respuesta_usuario == "b":
    print(
        "Incorrecto!"
    )
  elif respuesta_usuario == "c":
    print(
        "¡Incorrecto!"
    )
  elif respuesta_usuario == "d":
    print(
        "¡Correcto! La cultura Chimú, o también llamado el reino de Chimor, surgió en la costa norte de Perú entre los siglos XII y XV de nuestra era. Con su capital en Chan Chan actual departamento de La Libertad " 
    )
  print ()
  print(
    "\033[1;35m " + " Muy Bien!!! " + NombreR +
    ", veo que estas respondiendo las preguntas del ya complicado NIVEL DOS. Como soy tu amigo el Gran Socrates, eh venido a advertirte que la pregunta siguiente es la JEFE del NIVEL DOS, si la respondes correctamente, tendras un bono de ¡¡¡3 PUNTOS!!! que se sumara a tu puntaje obtenido. Muchos exitos y que la fuerza te acompañe"
    + '\033[0;m')
  input ()
  print("\033[4;31;41m" + "                                          " + '\033[0;m')
  print("\033[4;31;41m" + "  ██████╗░  ░█████╗░  ░██████╗  ░██████╗  " + '\033[0;m')
  print("\033[4;31;41m" + "  ██╔══██╗  ██╔══██╗  ██╔════╝  ██╔════╝  " + '\033[0;m')
  print("\033[4;31;41m" + "  ██████╦╝  ██║░░██║  ╚█████╗░  ╚█████╗░  " + '\033[0;m')
  print("\033[4;31;41m" + "  ██╔══██╗  ██║░░██║  ░╚═══██╗  ░╚═══██╗  " + '\033[0;m')
  print("\033[4;31;41m" + "  ██████╦╝  ╚█████╔╝  ██████╔╝  ██████╔╝  " + '\033[0;m')
  print("\033[4;31;41m" + "  ╚═════╝░  ░╚════╝░  ╚═════╝░  ╚═════╝░  " + '\033[0;m')
  print("\033[4;31;41m" + "                                          " + '\033[0;m')
  print()
  print(
    "\033[;31m12. En un torneo de tenis, el jugador que pierde se vuelve a casa. ¿Cuántos jugadores iniciaron este torneo si desde la ronda preliminar hasta la final se han jugado 128 partidos? \033[0;m")
  print()
  print("a) no se puede saber")
  print("b) 128")
  print("c) 64")
  print("d) 129")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ")
  print ()
  while respuesta_usuario not in ("a", "b", "c", "d"):
   respuesta_usuario = input("Debes responder a, b , c o d. Ingresa nuevamente tu respuesta: ")
  respuesta_correcta = "d"
  if respuesta_usuario == respuesta_correcta:
    print("¡Correcto! Tenemos que el jugador que pierde se va, es decir queda eliminado, por lo tanto, el total de partidos jugados es igual al total de personas eliminadas. Luego si hasta la final se juegan un total de 128 partidos, tenemos que se eliminan a un total de 128 personas, entonces queda una persona que es la persona que gana, asimismo, el total de jugadores es igual a los eliminados más el ganador, que será igual a 128 + 1 = 129 personas")
    respuestas_correctas = respuestas_correctas + 3
  elif respuesta_usuario == "a":
    print("¡Incorrecto!")
  elif respuesta_usuario == "b":
    print("¡Incorrecto!")
  elif respuesta_usuario == "c":
    print("¡Incorrecto!")
  elif respuesta_usuario == "d":
    print("¡Correcto! Tenemos que el jugador que pierde se va, es decir queda eliminado, por lo tanto, el total de partidos jugados es igual al total de personas eliminadas. Luego si hasta la final se juegan un total de 128 partidos, tenemos que se eliminan a un total de 128 personas, entonces queda una persona que es la persona que gana, asimismo, el total de jugadores es igual a los eliminados más el ganador, que será igual a 128 + 1 = 129 personas")
  print()

  print("ツツツTOMATE UN DESCANSOツツツ")
  print()
  print(" PUNTAJE DE LOS DOS PRIMEROS NIVELES: ")
  print()
  print("Puntos totales (+)")
  print(0 + respuestas_correctas) 
  print()
  print("PREGUNTAS TOTALES DEL PRIMER Y SEGUNDO NIVEL: 12 ")

  print()
  print ("\033[1;35m " + "Socrates:_IMPRESIONANTE!!! " + 
  NombreR + " Culminaste el temido NIVEL DOS, WOW, los dioses habitantes del Olimpo y yo te deseamos lo mejor en esta aventura. Pero, tiempos dificiles se acercan " + 
  NombreR + " . El nivel que viene ha sido elaborado por nada mas y nada menos que el terrorifico dios Hades, que implemento un poderoso hechizo para que sin importar la respuesta que dabas, te disminuiria puntos, pero Atenea se compadecio de ti, responde correctamente y tus puntos se multiplicaran, pero si te equivocas disminuiran, y terminaras debiendo puntaje."
    + '\033[0;m')
  print ()
  print ()
  import random  
  puntaje = random.randint(0, 5)

  print ("\033[4;34;43m" + "                                " + '\033[0;m')
  print ("\033[4;34;43m" + "_____❻『❻ NIVEL TRES ❻』❻_____  " + '\033[0;m')
  print ("\033[4;34;43m" + "                                " + '\033[0;m')
  print ()
  print ("13. ¿Cual es la obra lirica en la que se presenta uno de los mas grandes elogios funebres de la literatura castellana?")
  print ()
  print ("a) Don Rodrigo Manrrique ")
  print ("b) Es una muerte escogida")
  print ("c) Maria")
  print ("d) Cronicas de una muerte anunciada")
  print ("e) Coplas por la muerte de su padre")
  respuesta_usuario = input("\nTu respuesta: ")

  while respuesta_usuario not in ("a", "b", "c", "d", "e"):
   respuesta_usuario = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_usuario == "a":
    print ("Incorrecto")
    puntaje = puntaje - 5 
  elif respuesta_usuario == "b":
    print ("Incorrecto")
    puntaje = puntaje - 3
  elif respuesta_usuario == "c":
    print ("Incorrecto!")
    puntaje = puntaje - 1
  elif respuesta_usuario == "d":
    print ("Incorrecto!")
    puntaje = puntaje - 1
  else:
   puntaje = puntaje + 2
  print ("Muy bien!!! Las Coplas por la muerte de su padre, también citadas como Coplas a la muerte del maestre don Rodrigo o, simplemente, Las coplas de Jorge Manrique, son una elegía escrita por Jorge Manrique en la muerte de su padre, el maestre de Santiago Rodrigo Manrique. Escritas, al menos una parte, con posterioridad al 11 de noviembre de 1476, fecha de la muerte de Rodrigo Manrique, constituye una de las obras capitales de la literatura española.")
  print ()
  print (NombreR, "llevas", puntaje, "puntos")
  print ()
  print ("14. Una pareja acude a una consulta con un profesional en genetica y preguntan sobre cual es la probabilidad de que, sabiendo que el es daltonico y ella es una mujer de vision normal, pero portadora, puedan tener hijos daltonicos")
  print ()
  print ("a) 50%")
  print ("b) 40%")
  print ("c) 100%")
  print ("d) 25%")
  print ("e) 0% ")
  print ()
  respuesta_usuario = input("\nTu respuesta: ")
  while respuesta_usuario not in ("a", "b", "c", "d", "e"):
   respuesta_usuario = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_usuario == "b":
    print ("Incorrecto")
    puntaje = puntaje - 3
  elif respuesta_usuario == "c":
    print ("Incorrecto!")
    puntaje = puntaje - 1
  elif respuesta_usuario == "d":
    print ("Incorrecto!")
    puntaje = puntaje - 2
  elif respuesta_usuario == "e":
   print ("Incorrecto!")
   puntaje = puntaje - 2 
  else:
   print ("Muy bien!!! .")
   print ("El hombre daltónico será XdY. La mujer, al ser portadora, será XDXd.")
   print ("Cruce:         XdY     x     XDXd")
   print ("Gametos:     Xd    Y        XD   Xd")
   print ("Genotipos: XDXd   XdXd    XDY     XdY")
   print ("Conclusion: Es 50% probable que su descendencia ya sean de varones, mujeres o ambos, tengan daltonismo")
  puntaje = puntaje * 2
  print ()
  print ( NombreR, "llevas", puntaje, "puntos")
  print ()
  print ("15. ¿Que palabra esta correctamente separada en silabas?")
  print ()
  print ("a) He-roi-na")
  print ("b) Hio-i-des")
  print ("c) Coo-pe-ra-cion")
  print ("d) Eu-ca-ris-tia")
  print ("e) An-da-huay-las")
  print ()
  respuesta_usuario = input("\nTu respuesta: ")
  while respuesta_usuario not in ("a", "b", "c", "d", "e"):
   respuesta_usuario = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_usuario == "a":
   print ("Incorrecto")
   puntaje = puntaje - 3
  elif respuesta_usuario == "b":
    print ("Incorrecto!")
    puntaje = puntaje - 1
  elif respuesta_usuario == "c":
    print ("Incorrecto!")
    puntaje = puntaje - 2
  elif respuesta_usuario == "d":
    print ("Incorrecto!")
    puntaje = puntaje - 2 
  else:
    print (" La palabra Andahuaylas se divide en cuatro sílabas (An-da-huay-las ) y, por tanto, es tetrasílaba. La palabra Andahuaylas tiene tres sílabas átonas (An-da-huay-las). ")
    puntaje = puntaje * 2
  print()
  print ("16. Durante el desarrollo de la Segunda Guerra Mundial, ¿Que General aleman fue apodado como << El Zorro del desierto>>?")
  print ()
  print ("a) Erich von Manstein")
  print ("b) Erwin Rommel")
  print ("c) Heinz Guderian")
  print ("d) Friedrich Paulus")
  print ("e) Bernard Law Montgomery")
  print ()
  respuesta_usuario = input("\nTu respuesta: ")
  while respuesta_usuario not in ("a", "b", "c", "d", "e"):
    respuesta_usuario = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_usuario == "a":
    print ("Incorrecto")
    puntaje = puntaje - 4
  elif respuesta_usuario == "c":
    print ("Incorrecto!")
    puntaje = puntaje - 2
  elif respuesta_usuario == "d":
    print ("Incorrecto!")
    puntaje = puntaje / 2
  elif respuesta_usuario == "e":
    print ("Incorrecto!")
    puntaje = puntaje - 2 
  else:
   print ("¡¡¡CORRECTO!!!Johannes Erwin Eugen Rommel fue un general y estratega militar alemán. Popularmente apodado «El Zorro del Desierto», sirvió como mariscal de campo en la Wehrmacht de la Alemania nazi durante la Segunda Guerra Mundial. . ")
   puntaje = puntaje * 3
  print ()
  print (NombreR, "llevas", puntaje, "puntos")
  print ()
  print ("17. ¿Que lider chino, culmino la llamada <<Gran Revolucion Cultural>> iniciada en 1966 en China ")
  print ()
  print ("a) Mao Zedong")
  print ("b) Lin Biao")
  print ("c) Deng Xiaoping")
  print ("d) Zhang Chunqiao")
  print ("e) Qin Shi Huang")
  print ()
  respuesta_usuario = input("\nTu respuesta: ")
  while respuesta_usuario not in ("a", "b", "c", "d", "e"):
    respuesta_usuario = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_usuario == "a":
    print ("Incorrecto")
    puntaje = puntaje / 2
  elif respuesta_usuario == "b":
    print ("Incorrecto!")
    puntaje = puntaje - 2
  elif respuesta_usuario == "d":
    print ("Incorrecto!")
    puntaje = puntaje / 3
  elif respuesta_usuario == "e":
    print ("Incorrecto!")
    puntaje = puntaje - 2 
  else:
   print ("¡¡¡Correcto!!!En 1977, Deng Xiaoping propuso por primera vez la idea de <<Boluan Fanzheng>> para corregir los errores de la Revolución Cultural. El programa desmanteló gradualmente las políticas maoístas asociadas con la Revolución Cultural, rehabilitó a millones de víctimas que fueron perseguidas durante la Revolución, inició varias reformas sociopolíticas y devolvió el país al orden de manera sistemática")
  print()
  print (NombreR, "llevas", puntaje, "puntos")
  print ()
  print(
    "\033[1;35m " + " IMPRESIONANTE " + NombreR +
    " no te preocupes si has contestado de manera incorrecta, es solo un juego. El gran Socrates te va avisando que la pregunta siguiente es la JEFE del NIVEL TRES!!!, si la respondes correctamente, tendras un bono de ¡¡¡6 PUNTOS!!! que se sumara a tu puntaje obtenido. VAMOS!!!   POR LA VICTORIA...!!!"
    + '\033[0;m')
  print()
  print("\033[4;31;41m" + "███████████████████████████████████████████████████████████████" + '\033[0;m')
  print("\033[4;31;41m" + "█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀░░████░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█" + '\033[0;m')
  print("\033[4;31;41m" + "█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█" + '\033[0;m')
  print("\033[4;31;41m" + "███████████████████████████████████████████████████████████████" + '\033[0;m')
  print("\033[4;31;41m" + "                                                               " + '\033[0;m')
  print ()
  print ("\033[;31m18. En las interrelaciones biologicas, los seres vivos no estan aislados, sino que establecen relaciones dediversa indole. En el nivel intraespecifico, en el que algunas especies se diferencian morfologicamente de acuerdo a la funcion que realizan, estas relaciones son conocidas como... \033[0;m")
  print ()
  print ("a) Coloniales")
  print ("b) Cooperacion")
  print ("c) Amensalismo")
  print ("d) Sociedades")
  print ("e) Mutualismos")
  print ()
  respuesta_usuario = input("\nTu respuesta: ")
  while respuesta_usuario not in ("a", "b", "c", "d", "e"):
    respuesta_usuario = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_usuario == "a":
    print ("Incorrecto")
    puntaje = puntaje / 2
  elif respuesta_usuario == "b":
    print ("Incorrecto!")
    puntaje = puntaje - 2
  elif respuesta_usuario == "c":
    print ("Incorrecto!")
    puntaje = puntaje / 3
  elif respuesta_usuario == "e":
    print ("Incorrecto!")
    puntaje = puntaje - 2 
  else:
    print ("¡¡¡FELICIDADES!!! ¡¡¡CONTESTASTE CORRECTAMENTE!!!Las Sociedades son agrupaciones naturales o pactadas, organizadas para cooperar en la consecución de determinados fines”.")
  print ()
  print ("Alcanzaste", puntaje, "puntos en este nivel.")
  print()
  print()
  print("*** PUNTAJE FINAL ***")
  print("Puntos totales")
  print(puntaje + respuestas_correctas)
  print()
  print("TOTAL DE PREGUNTAS: 18 ")
  print()
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":
   print("\nEspero" , NombreR, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False 