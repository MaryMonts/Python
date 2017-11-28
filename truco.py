#-*-coding:UTF-8-*-

import random
import os

print ('*******************************************************************************************')
print ('******    Programação II -  2º Ciclo Jogos Digitais                                  ******')
print ('******   Nome Alexandre Nunes Dal Soglio           RA 1430961711035                  ******')
print ('*******************************************************************************************')

print '\n Bora Jogar um Truco \n '

# baralho
s = 1
sS = 1
sSs = 1
c = 1
cC = 1
cCc = 1
Vira = 1

# cartas na mao
opS = 1
opS2 = 1
opS3 = 1
opC = 1
opC2 = 1
opC3 = 1

CompVez = 1
Perg = 'd'
CompPontosPart = 0
SeusPontoPart = 0
CompPontosRod = 0
SeusPontosRod = 0
rodada = 0
choise = 0

# carta jogada
forcaJog = 0
forcaJog2 = 0
forcaJog3 = 0
forcaComp = 0
forcaComp2 = 0
forcaComp3 = 0


os.system("clear")


while CompPontosPart<12 and SeusPontoPart<12:
	opS = 1
	opS2 = 1
	opS3 = 1
	opC = 1
	opC2 = 1
	opC3 = 1
	CompPontosRod = 0
	SeusPontosRod = 0
	rodada = 0
	s = 1
	sS = 1
	sSs = 1
	c = 1
	cC = 1
	cCc = 1
	Vira = 1

	print raw_input('Embaralhando as cartas...')



	while CompPontosRod < 2 and SeusPontosRod < 2:
		Perg = 'd'
		choise = 0
		


		while(s == sS or s == sSs or s == Vira + 1 or s == Vira + 11 or s == Vira + 21 or s == Vira + 31 or s == Vira - 9 or s == Vira - 19 or s == Vira - 29 or s == Vira - 39 or s == c or s == cC or s == cCc or sS == sSs or sS == Vira + 1 or sS == Vira + 11 or sS == Vira + 21 or sS == Vira + 31 or sS == Vira - 9 or sS == Vira - 19 or sS == Vira - 29 or sS == Vira - 39 or sS == c or sS == cC or sS == cCc or sSs == Vira + 1 or sSs == Vira + 11 or sSs == Vira + 21 or sSs == Vira + 31 or sSs == Vira - 9 or sSs == Vira - 19 or sSs == Vira - 29 or sSs == Vira - 39 or sSs == c or sSs == cC or sSs == cCc or Vira == s or Vira == sS or Vira == sSs or Vira == c or Vira == cC or Vira == cCc or c == cC or c == cCc or c == Vira + 1 or c == Vira + 11 or c == Vira + 21 or c == Vira + 31 or c == Vira - 9 or c == Vira - 19 or c == Vira - 29 or c == Vira - 39 or cC == cCc or cC == Vira + 1 or cC == Vira + 11 or cC == Vira + 21 or cC == Vira + 31 or cC == Vira - 9 or cC == Vira - 19 or cC == Vira - 29 or cC == Vira - 39 or cCc == Vira + 1 or cCc == Vira + 11 or cCc == Vira + 21 or cCc == Vira + 31 or cCc == Vira - 9 or cCc == Vira - 19 or cCc == Vira - 29 or cCc == Vira - 39):

			s = random.randint(1,44)
			sS = random.randint(1,44)
			sSs = random.randint(1,44)
			Vira = random.randint(1,40)
			c = random.randint(1,44)
			cC = random.randint(1,44)
			cCc = random.randint(1,44)






		if s==1:
			y='4 de Ouro'
			forcaJog=1

		if sS==1:
			z='4 de Ouro'
			forcaJog2=1

		if sSs==1:
			w='4 de Ouro'
			forcaJog3=1

		if Vira==1:
			t='4 de Ouro'

		if s==2:
			y='5 de Ouro'
			forcaJog=5

		if sS==2:
			z='5 de Ouro'
			forcaJog2=5

		if sSs==2:
			w='5 de Ouro'
			forcaJog3=5

		if Vira==2:
			t='5 de Ouro'

		if s==3:
			y='6 de Ouro'
			forcaJog=9

		if sS==3:
			z='6 de Ouro'
			forcaJog2=9

		if sSs==3:
			w='6 de Ouro'
			forcaJog3=9

		if Vira==3:
			t='6 de Ouro'

		if s==4:
			y='7 de Ouro'
			forcaJog=13

		if sS==4:
			z='7 de Ouro'
			forcaJog2=13

		if sSs==4:
			w='7 de Ouro'
			forcaJog3=13

		if Vira==4:
			t='7 de Ouro'

		if s==5:
			y='Dama de Ouro'
			forcaJog=17

		if sS==5:
			z='Dama de Ouro'
			forcaJog2=17

		if sSs==5:
			w='Dama de Ouro'
			forcaJog3=17

		if Vira==5:
			t='Dama de Ouro'

		if s==6:
			y='Valete de Ouro'
			forcaJog=21

		if sS==6:
			z='Valete de Ouro'
			forcaJog2=21

		if sSs==6:
			w='Valete de Ouro'
			forcaJog3=21

		if Vira==6:
			t='Valete de Ouro'

		if s==7:
			y='Reis de Ouro'
			forcaJog=25

		if sS==7:
			z='Reis de Ouro'
			forcaJog2=25

		if sSs==7:
			w='Reis de Ouro'
			forcaJog3=25

		if Vira==7:
			t='Reis de Ouro'

		if s==8:
			y='As de Ouro'
			forcaJog=29

		if sS==8:
			z='As de Ouro'
			forcaJog2=29

		if sSs==8:
			w='As de Ouro'
			forcaJog3=29

		if Vira==8:
			t='As de Ouro'

		if s==9:
			y='2 de Ouro'
			forcaJog=33

		if sS==9:
			z='2 de Ouro'
			forcaJog2=33

		if sSs==9:
			w='2 de Ouro'
			forcaJog3=33

		if Vira==9:
			t='2 de Ouro'

		if s==10:
			y='3 de Ouro'
			forcaJog=37

		if sS==10:
			z='3 de Ouro'
			forcaJog2=37

		if sSs==10:
			w='3 de Ouro'
			forcaJog3=37

		if Vira==10:
			t='3 de Ouro'

		if s==41:
			y='Sete Ouro'
		forcaJog=41
			
		if sS==41:
			z='Sete Ouro'
			forcaJog2=41			

		if sSs==41:
			w='Sete Ouro'
			forcaJog3=41
			




		if Vira==41:
			t='5 de Espada'

		if s==11:
			y='4 de Espada'
			forcaJog=2

		if sS==11:
			z='4 de Espada'
			forcaJog2=2

		if sSs==11:
			w='4 de Espada'
			forcaJog3=2

		if Vira==11:
			t='4 de Espada'

		if s==12:
			y='5 de Espada'
			forcaJog=6

		if sS==12:
			z='5 de Espada'
			forcaJog2=6

		if sSs==12:
			w='5 de Espada'
			forcaJog3=6

		if Vira==12:
			t='5 de Espada'

		if s==13:
			y='6 de Espada'
			forcaJog=10

		if sS==13:
			z='6 de Espada'
			forcaJog2=10

		if sSs==13:
			w='6 de Espada'
			forcaJog3=10

		if Vira==13:
			t='6 de Espada'

		if s==14:
			y='7 de Espada'
			forcaJog=14

		if sS==14:
			z='7 de Espada'
			forcaJog2=14

		if sSs==14:
			w='7 de Espada'
			forcaJog3=14

		if Vira==14:
			t='7 de Espada'

		if s==15:
			y='Dama de Espada'
			forcaJog=18

		if sS==15:
			z='Dama de Espada'
			forcaJog2=18

		if sSs==15:
			w='Dama de Espada'
			forcaJog3=18

		if Vira==15:
			t='Dama de Espada'

		if s==16:
			y='Valete de Espada'
			forcaJog=22

		if sS==16:
			z='Valete de Espada'
			forcaJog2=22

		if sSs==16:
			w='Valete de Espada'
			forcaJog3=22

		if Vira==16:
			t='Valete de Espada'

		if s==17:
			y='Reis de Espada'
			forcaJog=26

		if sS==17:
			z='Reis de Espada'
			forcaJog2=26

		if sSs==17:
			w='Reis de Espada'
			forcaJog3=26

		if Vira==17:
			t='Reis de Espada'

		if s==18:
			y='As de Espada'
			forcaJog=30

		if sS==18:
			z='As de Espada'
			forcaJog2=30

		if sSs==18:
			w='As de Espada'
			forcaJog3=30

		if Vira==18:
			t='As de Espada'

		if s==19:
			y='2 de Espada'
			forcaJog=34

		if sS==19:
			z='2 de Espada'
			forcaJog2=34

		if sSs==19:
			w='2 de Espada'
			forcaJog3=34

		if Vira==19:
			t='2 de Espada'

		if s==20:
			y='3 de Espada'
			forcaJog=38

		if sS==20:
			z='3 de Espada'
			forcaJog2=38

		if sSs==20:
			w='3 de Espada'
			forcaJog3=38

		if Vira==20:
			t='3 de Espada'

		if s==42:
			y='Espadilha'
			forcaJog=42
			
		if sS==42:
			z='Espadilha'
			forcaJog2=42
			
		if sSs==42:
			w='Espadilha'
			forcaJog3=42



			
		if Vira==42:
			t='7 de Copas'

		if s==21:
			y='4 de Copas'
			forcaJog=3

		if sS==21:
			z='4 de Copas'
			forcaJog2=3

		if sSs==21:
			w='4 de Copas'
			forcaJog3=3

		if Vira==21:
			t='4 de Copas'

		if s==22:
			y='5 de Copas'
			forcaJog=7

		if sS==22:
			z='5 de Copas'
			forcaJog2=7

		if sSs==22:
			w='5 de Copas'
			forcaJog3=7

		if Vira==22:
			t='5 de Copas'

		if s==23:
			y='6 de Copas'
			forcaJog=11

		if sS==23:
			z='6 de Copas'
			forcaJog2=11

		if sSs==23:
			w='6 de Copas'
			forcaJog3=11

		if Vira==23:
			t='6 de Copas'
			forcaJog=11

		if s==24:
			y='7 de Copas'
			forcaJog=15

		if sS==24:
			z='7 de Copas'
			forcaJog2=15

		if sSs==24:
			w='7 de Copas'
			forcaJog3=15

		if Vira==24:
			t='7 de Copas'

		if s==25:
			y='Dama de Copas'
			forcaJog=19

		if sS==25:
			z='Dama de Copas'
			forcaJog2=19

		if sSs==25:
			w='Dama de Copas'
			forcaJog3=19

		if Vira==25:
			t='Dama de Copas'

		if s==26:
			y='Valete de Copas'
			forcaJog=23

		if sS==26:
			z='Valete de Copas'
			forcaJog2=23

		if sSs==26:
			w='Valete de Copas'
			forcaJog3=23

		if Vira==26:
			t='Valete de Copas'

		if s==27:
			y='Reis de Copas'
			forcaJog=27

		if sS==27:
			z='Reis de Copas'
			forcaJog2=27

		if sSs==27:
			w='Reis de Copas'
			forcaJog3=27

		if Vira==27:
			t='Reis de Copas'

		if s==28:
			y='As de Copas'
			forcaJog=31

		if sS==28:
			z='As de Copas'
			forcaJog2=31

		if sSs==28:
			w='As de Copas'
			forcaJog3=31

		if Vira==28:
			t='As de Copas'

		if s==29:
			y='2 de Copas'
			forcaJog=35

		if sS==29:
			z='2 de Copas'
			forcaJog2=35

		if sSs==29:
			w='2 de Copas'
			forcaJog3=35

		if Vira==29:
			t='2 de Copas'

		if s==30:
			y='3 de Copas'
			forcaJog=39

		if sS==30:
			z='3 de Copas'
			forcaJog2=39

		if sSs==30:
			w='3 e Copas'
			forcaJog3=39

		if Vira==30:
			t='3 de Copas'

		if s==43:
			y='Sete Copas'
			forcaJog=43
			
		if sS==43:
			z='Sete Copas'
			forcaJog2=43
			
		if sSs==43:
			w='Sete Copas'
			forcaJog3=43
			



		if Vira==43:
			t='4 de Paus'

		if s==31:
			y='4 de Paus'
			forcaJog=4

		if sS==31:
			z='4 de Paus'
			forcaJog2=4

		if sSs==31:
			w='4 de Paus'
			forcaJog3=4

		if Vira==31:
			t='4 de Paus'
			forcaJog=4

		if s==32:
			y='5 de Paus'
			forcaJog=8

		if sS==32:
			z='5 de Paus'
			forcaJog2=8

		if sSs==32:
			w='5 de Paus'
			forcaJog3=8

		if Vira==32:
			t='5 de Paus'

		if s==33:
			y='6 de Paus'
			forcaJog=12

		if sS==33:
			z='6 de Paus'
			forcaJog2=12

		if sSs==33:
			w='6 de Paus'
			forcaJog3=12

		if Vira==33:
			t='6 de Paus'

		if s==34:
			y='7 de Paus'
			forcaJog=16

		if sS==34:
			z='7 de Paus'
			forcaJog2=16

		if sSs==34:
			w='7 de Paus'
			forcaJog3=16

		if Vira==34:
			t='7 de Paus'

		if s==35:
			y='Dama de Paus'
			forcaJog=20

		if sS==35:
			z='Dama de Paus'
			forcaJog2=20

		if sSs==35:
			w='Dama de Paus'
			forcaJog3=20

		if Vira==35:
			t='Dama de Paus'

		if s==36:
			y='Valete de Paus'
			forcaJog=24

		if sS==36:
			z='Valete de Paus'
			forcaJog2=24

		if sSs==36:
			w='Valete de Paus'
			forcaJog3=24

		if Vira==36:
			t='Valete de Paus'

		if s==37:
			y='Reis de Paus'
			forcaJog=28

		if sS==37:
			z='Reis de Paus'
			forcaJog2=28

		if sSs==37:
			w='Reis de Paus'
			forcaJog3=28

		if Vira==37:
			t='Reis de Paus'

		if s==38:
			y='As de Paus'
			forcaJog=32

		if sS==38:
			z='As de Paus'
			forcaJog2=32

		if sSs==38:
			w='As de Paus'
			forcaJog3=32

		if Vira==38:
			t='As de Paus'

		if s==39:
			y='2 de Paus'
			forcaJog=36

		if sS==39:
			z='2 de Paus'
			forcaJog2=36

		if sSs==39:
			w='2 de Paus'
			forcaJog3=36

		if Vira==39:
			t='2 de Paus'

		if s==40:
			y='3 de Paus'
			forcaJog=40

		if sS==40:
			z='3 de Paus'
			forcaJog2=40

		if sSs==40:
			w='3 de Paus'
			forcaJog3=40

		if Vira==40:
			t='3 de Paus'

		if s==44:
			y='Zap'
			forcaJog=44
		
		if sS==44:
			z='Zap'
			forcaJog2=44
			
		if sSs==44:
			w='Zap'
			forcaJog3=44
			
		if Vira==44:
			t='6 de Ouro'




		if c==1:
			yy='4 de Ouro'
			forcacomp=1

		if cC==1:
			zz='4 de Ouro'
			forcacomp2=1

		if cCc==1:
			ww='4 de Ouro'
			forcacomp3=1

		if c==2:
			yy='5 de Ouro'
			forcacomp=5

		if cC==2:
			zz='5 de Ouro'
			forcacomp2=5

		if cCc==2:
			www='5 de Ouro'
			forcacomp3=5

		if c==3:
			yy='6 de Ouro'
			forcacomp=9

		if cC==3:
			zz='6 de Ouro'
			forcacomp2=9

		if cCc==3:
			ww='6 de Ouro'
			forcacomp3=9

		if c==4:
			yy='7 de Ouro'
			forcacomp=13

		if cC==4:
			zz='7 de Ouro'
			forcacomp2=13

		if cCc==4:
			ww='7 de Ouro'
			forcacomp3=13

		if c==5:
			yy='Dama de Ouro'
			forcacomp=17

		if cC==5:
			zz='Dama de Ouro'
			forcacomp2=17

		if cCc==5:
			ww='Dama de Ouro'
			forcacomp3=17

		if c==6:
			yy='Valete de Ouro'
			forcacomp=21

		if cC==6:
			zz='Valete de Ouro'
			forcacomp2=21

		if cCc==6:
			ww='Valete de Ouro'
			forcacomp3=21

		if c==7:
			yy='Reis de Ouro'
			forcacomp=25

		if cC==7:
			zz='Reis de Ouro'
			forcacomp2=25

		if cCc==7:
			ww='Reis de Ouro'
			forcacomp3=25

		if c==8:
			yy='As de Ouro'
			forcacomp2=29

		if cC==8:
			zz='As de Ouro'
			forcacomp3=29

		if cCc==8:
			ww='As de Ouro'
			forcacomp2=29

		if c==9:
			yy='2 de Ouro'
			forcacomp3=33

		if cC==9:
			zz='2 de Ouro'
			forcacomp2=33

		if cCc==9:
			ww='2 de Ouro'
			forcacomp3=33

		if c==10:
			yy='3 de Ouro'
			forcacomp=37

		if cC==10:
			zz='3 de Ouro'
			forcacomp2=37

		if cCc==10:
			ww='3 de Ouro'
			forcacomp3=37

		if c==41:
			yy='Sete Ouro'
			forcacomp=41
			
		if cC==41:
			zz='Sete Ouro'
			forcacomp2=41
			
		if cCc==41:
			ww='Sete Ouro'
			forcacomp3=41
			


		if c==11:
			yy='4 de Espada'
			forcacomp=2

		if cC==11:
			zz='4 de Espada'
			forcacomp2=2

		if cCc==11:
			ww='4 de Espada'
			forcacomp3=2

		if c==12:
			yy='5 de Espada'
			forcacomp=6

		if cC==12:
			zz='5 de Espada'
			forcacomp2=6

		if cCc==12:
			ww='5 de Espada'
			forcacomp3=6

		if c==13:
			yy='6 de Espada'
			forcacomp=10

		if cC==13:
			zz='6 de Espada'
			forcacomp2=10

		if cCc==13:
			ww='6 de Espada'
			forcacomp3=10

		if c==14:
			yy='7 de Espada'
			forcacomp=14

		if cC==14:
			zz='7 de Espada'
			forcacomp2=14

		if cCc==14:
			ww='7 de Espada'
			forcacomp3=14

		if c==15:
			yy='Dama de Espada'
			forcacomp=18

		if cC==15:
			zz='Dama de Espada'
			forcacomp2=18

		if cCc==15:
			ww='Dama de Espada'
			forcacomp3=18

		if c==16:
			yy='Valete de Espada'
			forcacomp=22

		if cC==16:
			zz='Valete de Espada'
			forcacomp2=22

		if cCc==16:
			ww='Valete de Espada'
			forcacomp3=22

		if c==17:
			yy='Reis de Espada'
			forcacomp=26

		if cC==17:
			zz='Reis de Espada'
			forcacomp2=26

		if cCc==17:
			ww='Reis de Espada'
			forcacomp3=26

		if c==18:
			yy='As de Espada'
			forcacomp=30

		if cC==18:
			zz='As de Espada'
			forcacomp2=30

		if cCc==18:
			ww='As de Espada'
			forcacomp3=30

		if c==19:
			yy='2 de Espada'
			forcacomp=34

		if cC==19:
			zz='2 de Espada'
			forcacomp2=34

		if cCc==19:
			ww='2 de Espada'
			forcacomp3=34

		if c==20:
			yy='3 de Espada'
			forcacomp=38

		if cC==20:
			zz='3 de Espada'
			forcacomp2=38

		if cCc==20:
			ww='3 de Espada'
			forcacomp3=38

		if c==42:
			yy='Espadilha'
			forcacomp=42
			
		if cC==42:
			zz='Espadilha'
			forcacomp2=42
			
		if cCc==42:
			ww='Espadilha'
			forcacomp3=42
			


		if c==21:
			yy='4 de Copas'
			forcacomp=3

		if cC==21:
			zz='4 de Copas'
			forcacomp2=3

		if cCc==21:
			ww='4 de Copas'
			forcacomp3=3

		if c==22:
			yy='5 de Copas'
			forcacomp=7

		if cC==22:
			zz='5 de Copas'
			forcacomp2=7

		if cCc==22:
			ww='5 de Copas'
			forcacomp3=7

		if c==23:
			yy='6 de Copas'
			forcacomp=11

		if cC==23:
			zz='6 de Copas'
			forcacomp2=11

		if cCc==23:
			ww='6 de Copas'
			forcacomp3=11

		if c==24:
			yy='7 de Copas'
			forcacomp=15

		if cC==24:
			zz='7 de Copas'
			forcacomp2=15

		if cCc==24:
			ww='7 de Copas'
			forcacomp3=15

		if c==25:
			yy='Dama de Copas'
			forcacomp=19

		if cC==25:
			zz='Dama de Copas'
			forcacomp2=19

		if cCc==25:
			ww='Dama de Copas'
			forcacomp3=19

		if c==26:
			yy='Valete de Copas'
			forcacomp=23

		if cC==26:
			zz='Valete de Copas'
			forcacomp2=23

		if cCc==26:
			ww='Valete de Copas'
			forcacomp3=23

		if c==27:
			yy='Reis de Copas'
			forcacomp=27

		if cC==27:
			zz='Reis de Copas'
			forcacomp2=27

		if cCc==27:
			ww='Reis de Copas'
			forcacomp3=27

		if c==28:
			yy='As de Copas'
			forcacomp=31

		if cC==28:
			zz='As de Copas'
			forcacomp2=31

		if cCc==28:
			ww='As de Copas'
			forcacomp3=31

		if c==29:
			yy='2 de Copas'
			forcacomp=35

		if cC==29:
			zz='2 de Copas'
			forcacomp2=35

		if cCc==29:
			ww='2 de Copas'
			forcacomp3=35

		if c==30:
			yy='3 de Copas'
			forcacomp=39

		if cC==30:
			zz='3 de Copas'
			forcacomp2=39

		if cCc==30:
			ww='3 de Copas'
			forcacomp3=39

		if c==43:
			yy='Sete Copas'
			forcacomp=43
			
		if cC==43:
			zz='Sete Copas'
			forcacomp2=43
			
		if cCc==43:
			ww='Sete Copas'
			forcacomp3=43
			


		if c==31:
			yy='4 de Paus'
			forcacomp=4

		if cC==31:
			zz='4 de Paus'
			forcacomp2=4

		if cCc==31:
			ww='4 de Paus'
			forcacomp3=4

		if c==32:
			yy='5 de Paus'
			forcacomp=8

		if cC==32:
			zz='5 de Paus'
			forcacomp2=8

		if cCc==32:
			ww='5 de Paus'
			forcacomp3=8

		if c==33:
			yy='6 de Paus'
			forcacomp=12

		if cC==33:
			zz='6 de Paus'
			forcacomp2=12

		if cCc==33:
			ww='6 de Paus'
			forcacomp3=12

		if c==34:
			yy='7 de Paus'
			forcacomp=16

		if cC==34:
			zz='7 de Paus'
			forcacomp2=16

		if cCc==34:
			ww='7 de Paus'
			forcacomp3=16

		if c==35:
			yy='Dama de Paus'
			forcacomp=20

		if cC==35:
			zz='Dama de Paus'
			forcacomp2=20

		if cCc==35:
			ww='Dama de Paus'
			forcacomp3=20

		if c==36:
			yy='Valete de Paus'
			forcacomp=24

		if cC==36:
			zz='Valete de Paus'
			forcacomp2=24

		if cCc==36:
			ww='Valete de Paus'
			forcacomp3=24

		if c==37:
			yy='Reis de Paus'
			forcacomp=28

		if cC==37:
			zz='Reis de Paus'
			forcacomp2=28

		if cCc==37:
			ww='Reis de Paus'
			forcacomp3=28

		if c==38:
			yy='As de Paus'
			forcacomp=32

		if cC==38:
			zz='As de Paus'
			forcacomp2=32

		if cCc==38:
			ww='As de Paus'
			forcacomp3=32

		if c==39:
			yy='2 de Paus'
			forcacomp=36

		if cC==39:
			zz='2 de Paus'
			forcacomp2=36

		if cCc==39:
			ww='2 de Paus'
			forcacomp3=36

		if c==40:
			yy='3 de Paus'
			forcacomp=40

		if cC==40:
			zz='3 de Paus'
			forcacomp2=40

		if cCc==40:
			ww='3 de Paus'
			forcacomp3=40


		if c==44:
			yy='Zap'
			forcacomp=44
			
		if cC==44:
			zz='Zap'
			forcacomp2=44
			
		if cCc==44:
			ww='Zap'
			forcacomp3=44
			




		print ''
		print ''
		print ''
		print '               Suas Cartas                                Vira'
		print '-'*40 + '|' + '-'*40
		if opS==1:
			print 'Carta A: %s'%y
		if opS2==1:
			print 'Carta B: %s                                   %s' %(z,t)
		if opS3==1:
			print 'Carta C: %s'%w
		print ''
		print ''

		while Perg != 'a' and Perg != 'b' and Perg != 'c':
			print ''
			if opS==1 and opS2==1 and opS3==1:
				while Perg != 'a' and Perg != 'b' and Perg != 'c':
					Perg = str(raw_input('Escolha a carta desejada:(a ou b ou c)'))
			elif opS==1 and opS2==1 and opS3==0:
				while Perg != 'a' and Perg != 'b':
					Perg = str(raw_input('Escolha a carta desejada:(a ou b)'))
			elif opS==1 and opS2==0 and opS3==0:
				while Perg != 'a':
					Perg = str(raw_input('Escolha a carta desejada:(somente a)'))
			elif opS==0 and opS2==1 and opS3==0:
				while Perg != 'b':
					Perg = str(raw_input('Escolha a carta desejada:(somente b)'))
			elif opS==0 and opS2==0 and opS3==1:
				while Perg != 'c':
					Perg = str(raw_input('Escolha a carta desejada:(somente c)'))
			elif opS==0 and opS2==1 and opS3==1:
				while Perg != 'b' and Perg != 'c':
					Perg = str(raw_input('Escolha a carta desejada:(b ou c)'))
			elif opS==1 and opS2==0 and opS3==1:
				while Perg != 'a' and Perg != 'c':
					Perg = str(raw_input('Escolha a carta desejada:(a ou c)'))



		print ''
		if Perg == 'a':
			print'                %s'%y
			choise = forcaJog
			opS=0

		if Perg == 'b':
			print'                %s'%z
			choise = forcaJog2
			opS2=0

		if Perg == 'c':
			print'                %s'%w
			choise = forcaJog3
			opS3=0

		print ''
		print raw_input('Computador esta escolhendo uma carta...')



		if opC==1 and opC2==1 and opC3==1:
			if forcacomp>forcacomp2 and forcacomp>forcacomp3:
				CompVez = 1
			elif forcacomp2>forcacomp and forcacomp2>forcacomp3:
				CompVez = 2
			elif forcacomp3>forcacomp and forcacomp3>forcacomp2:
				CompVez = 3
			if choise > forcacomp and choise > forcacomp2 and 					choise 	> forcacomp3:
				if forcacomp<forcacomp2 and forcacomp<forcacomp3:
					CompVez = 1
				elif forcacomp2<forcacomp and forcacomp2<forcacomp3:
					CompVez = 2
				elif forcacomp3<forcacomp and forcacomp3<forcacomp2:
					CompVez = 3


		elif opC==0 and opC2==1 and opC3==1:
			CompVez = random.randint(2,3)

		elif opC==1 and opC2==1 and opC3==0:
			CompVez = random.randint(1,2)

		elif opC==1 and opC2==0 and opC3==1:
			CompVez = random.randint(1,3)
			while CompVez == 2:
				CompVez = random.randint(1,3)

		elif opC==1 and opC2==0 and opC3==0:
			CompVez = 1

		elif opC==0 and opC2==1 and opC3==0:
			CompVez = 2

		elif opC==0 and opC2==0 and opC3==1:
			CompVez = 3



		if CompVez == 1:
			opC=0
			print '       Computador jogou %s'%yy
			if choise < forcacomp:
				CompPontosRod = CompPontosRod + 1
			else:
				SeusPontosRod = SeusPontosRod + 1

			print ''

		if CompVez == 2:
			opC2=0
			print '       Computador jogou %s'%zz
			if choise < forcacomp2:
				CompPontosRod = CompPontosRod + 1
			else:
				SeusPontosRod = SeusPontosRod + 1
			print ''

		if CompVez == 3:
			opC3=0
			print '       Computador jogou %s'%ww
			if choise < forcacomp3:
				CompPontosRod = CompPontosRod + 1
			else:
				SeusPontosRod = SeusPontosRod + 1
			print ''

		
		rodada = rodada + 1

		print ''
		print ''
		print '			Rodada: %d'%rodada
		print '			Seus pontos na rodada: %d'%SeusPontosRod
		print '			Pontos do Computador na rodada: %d'%CompPontosRod
		print '                        ------------Partida------------'
		print '                        Voce:   %d   Computador:   %d' %(SeusPontoPart,CompPontosPart)


		print ''
		print ''

		if SeusPontosRod == 2:
			SeusPontoPart = SeusPontoPart + 1

		if CompPontosRod == 2:
			CompPontosPart = CompPontosPart + 1

		print ''
		print ''
		print ''
		print ''

		print raw_input('Aperte qualquer tecla para continuar...')
		os.system("clear")

if CompPontosPart >= 12:
	print '			     VOCE PERDEU!			'

elif SeusPontoPart >=12:
	print '			!! VOCE GANHOU!!!		'

print ''
print ''
print ''
