from colorama import init
from colorama import Fore, Back, Style
init()

what = input ("Какой цвет тебе нравится больше? (Красный, зеленый, желтый):")

if what == "красный":
    print ( Back.RED )
    what = input ("То есть, если фон за буквами будет таким, тебе будет приятно? (да, нет)")
elif what == "зеленый":
    print ( Back.GREEN )
    what = input ("То есть, если фон за буквами будет таким, тебе будет приятно? (да, нет)")
elif what == "зелёный":
    print ( Back.GREEN )
    what = input ("То есть, если фон за буквами будет таким, тебе будет приятно? (да, нет)")
elif what == "желтый":
    print ( Back.YELLOW )
    what = input ("То есть, если фон за буквами будет таким, тебе будет приятно? (да, нет)")
elif what == "жёлтый":
    print ( Back.YELLOW )
    what = input ("То есть, если фон за буквами будет таким, тебе будет приятно? (да, нет)")


if what == "да":
    print ("ну и хорошо")
elif what == "нет":
    print ( Back.BLACK )
    print ("ничего страшного, я только учусь :)")

name = input ("Как тебя зовут? ")
print ("Привет " + name + "! Какое красивое у тебя имя :)")
age = input ("Сколько тебе лет? ")
print (age + "?! Это же прекрасный возраст!\nУ меня еще небольшой лексикон. Приходи завтра. С тобой круто!")
       
input ()
