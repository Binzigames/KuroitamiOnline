#-------------> logos
import pyfiglet
logo = pyfiglet.figlet_format("Kuroitami Online", font="doom")
logo_studio = pyfiglet.figlet_format("Mizumi Studio", font="roman")

#-------------> arts
# drop here arts with [""] < list
#sys.stdout.write(Fore.WHITE + "\n".join(line[0] for line in art) + "\n") < use that to draw them

loading_screen = [
['&&&&&&&&&&&&&$$Xx++;;;;:::::::::::::::::::::::::::::::::::::::;;;+xX$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'],
['&&&&&&&&&$Xxx+;;;;;;;;;;:;;;;;;;;;:::::::::::::::::::::::::::::::::;;;+xX$&&&&&&&&&&&&&&&&&&&&&&&&&&'],
['&&&&&$$xx+;;;;;;;;;;;;;;;;;;;;;;;;;:::::::::::::::::::::::::::::::::::::;;+xX$&&&&&&&&&&&&&&&&&&&&&&'],
['&&$Xx++;;;;;;;;;;;;;;;;:::;;;;::;;:::::::::::::::::::::::::::::::::::::::::;;;+xX&&&&&&&&&&&&&&&&&&&'],
['Xx+;;;;;;;;;;;;;;;;;;;::::::::;::::::::::::::::::::::::::::::::::::::::::::::::;;+x$&&&&&&&&&&&&&&&&'],
[';;;;;;;;;;;;;;;;;;;;;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;+x$&&&&&&&&&&&&&'],
[':;;;;;;;;;;;;;;;;;;;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;+X$&&&&&&&&&&'],
[':;;;;;;;;;;;;;;;::::;xxx+;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;+x$&&&&&&&&'],
[':;;;;;;;;;;;;;;::::::+xx+;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;xX&&&&&&'],
[':;;;;;;;;::::::::::::+XX+;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;+X&&&&'],
[':::::::::::::::::::::+x+;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;xX&&'],
[':::::::::::::::::::::+x+;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;+x$'],
[':::::::::::::::::::::xXX+;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;+X'],
[':::::::::::::::::::::+x+;:::::::::::::::::::::::::::::::::::::::;;:::+;:;;;:;::;;:::::::::::::::;;+X'],
[':::::::::::::::::::::xXXx;:::::::::::::::::::::::::::::::::::::::X$$X;::::::::+$X;;:::::::::::::;;+X'],
[':::::::::::::::::::::;++;;::::::::::::::::::::::::::::::::::;xx$$$$$$$$$$$x++xx;;:::::::::::::::;;+X'],
['::::::::::::::::::::;+XX+;:::::::::::::::::::::::::::::::::xX$$$$$$$$$$x;:::::::::::::::::::::::;;+X'],
['::::::::::::::+++;:;++Xx++::::::::::::::::::::::::::::::::::::::::::;;;::::::::::::::::::::::::::;+X'],
[':::::+xxxxxxxXxXXxXXXXXXxXXX+:::::::::::;::::::::::::::::::::::::::::::::::::::::::::::::::::::::;+X'],
[':::::+xxxxxxxXXXXXxxxxxx+xX$x+::::::::::x;:::::::::::::::::::::::::::::::::::::::::::::::::::::::;;X'],
[':::;xxxxxxxxxxxxXXxxxxxxx+X$$XxX;:::;:XxXx;:;;;::::::::::::::::::::::::::::::::::::::::::::::::::;;X'],
[':+xxXXXXXXXXXXXXXXxxxxxxXxX$$$X$$XXXXXX$$X+xXXx+:::::::::::::::::::::::::::::::::::::::::::::::::;;x'],
['+xXxxxxxxxxxxxxxXXxxxxxxXX$$$$$X$$$$$$$$$$++XXxxxx+;;;;;;;;;;;;;;;;;::::xXXxXXXXXXXXXXxxx::::::::;;x'],
['xXxxxxxxxxxxxxxxXXXXXXXXXX$$$$$$$$$$$$$XXXxxXXxxx++++xxx+xxxx+xxx+xx++:;xXXXXXXXXXXXXXxxx+;;;++++x+X'],
['xXXxxxxxxxxXX$$$$$XXxXx+XXXXxxXXXXXXXXXXXX++xxx++++++++++++++++++++xxxxxxXXXXXXXXXXXXXXxxxxxxxxxXXX$'],
['XXxxxxxxxXXXXXXXxxXXXXxxxXxx+xX$XXXxXXXXxX;:xxx+x+++++++++++++++++++xxxXxXXXXXXXXXXXXXXxxxxxxxxxxxxX'],
['xxx+;;;;;;;;::;xxxx+xxxxxxxxxxxxxxxxxxxxxxXXXXXx+xxxxxxxxXXX$XXXXXxxxxxXx+++++++++++++++xxx$xxxxXXXX'],
[':+++xxXXXXXXXXXXx+;;xxxxxXxx;XXXXXXxXxxXXxx$XXxxxxxxxx+++xxX$$$$XX+xxxxXx+++++++++++++++XXX$XXXXXXX$'],
['xxxxxxxX$$X$Xxxx++++;xxxxXXxxxXXx+++x;+xx+;xXXXXXXXXXXXxx+++++++xx+++++++++x++++++++++++XxX$Xxxxx++X'],
[';++;;;;;;;xxx++++++;;;++x+x+++xxXXXXX$XXXXXXXXXxXXXXXXXxXxxxxxXXxxXxxxxxxxxxxxxxxxxxxxxxXX$$XX++x++x'],
[';+++;;;;;;;;;+;;;;;;;;+++x++xXXXXXx+xx+++xxxxxxx++xxx+;;XXx+;++;;XXXXXXXXXX$xxXXXXXXXXX$XXXXx$$$xx+x'],
['+x+;++++xx+x+;+++;;;+;xx+x+xx++++XxxxXX$$XXXX$XX$XX$X;Xx+xxXXXXxXXXXxx$$XxX$XXXx;++xXXXX++xXX$$$$Xxx'],
['Xxx;:+xxXXxxx+++xXXx+;x$Xx++++++xXXXXXXXxxxxXX+xxX$$xXXXX$XXXXxXXX$$XXX$$XX$XX$XX$XXX$XXX$X$$X$$XXXX'],
['x;xXXxxX$$X+++xxxxXX+xXXXXX$$$xXxx$XXXXxxxX$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$xXX$&&$X$X$$$$xX$XX$X'],
['XX$XXxXX$$X+xXxXXxx+;xXXXxxxxXXX$$X$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$$$X$&&$$XxXxX$$X$XxX$'],
['XxXxxxxXXxX$$x++xxxXXX$$X$XXX$XX$$$$$$$$$$$$$$$$$$$$$$$X$$$$$$$$X$$$X$$$XX$$$XX$XXx$$$$X$XXX$XXXXXXX']
]