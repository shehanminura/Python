print('point Table')
print('pak= 7 \nNewZ =8 \nAfg=7')
print('There are three matches between them.')

pak_vs_NZ=input('pakistan vs New zealand match=')
pak_vs_afg=input('pakisthan vs afgnistan match=')
NZ_vs_agf=input('afganistan vs New zealand match=')

pak_net_rate=input('pakisthan net  run rate= ')
afg_net_rate=input('Afganisthan net run rate=')
NZ_net_rate=input('NewZeland net run rate=')

#print the team who slected to semi

if NZ_vs_agf=="NZwon" and pak_vs_afg=="pakwon" and pak_vs_NZ=="pakwon":
    if pak_net_rate<NZ_net_rate:
        print("NewZeland is selected to semi")
    else:
        print("pakisthan is selected to semi")

if NZ_vs_agf=="afgwon" and pak_vs_afg=="pakwon" and pak_vs_NZ=="pakwon":
    print("pakisthan is selected to semi")

if NZ_vs_agf=="afgwon" and pak_vs_afg=="pakwon" and pak_vs_NZ=="NZwon":
    print("NewZeland is selected to semi")

if NZ_vs_agf=="afgwon" and pak_vs_afg=="afgwon" and pak_vs_NZ=="pakwon":
    print("Afganisthan is selected to semi")

if NZ_vs_agf=="NZwon" and pak_vs_afg=="pakwon" and pak_vs_NZ=="NZwon":
    print(" NewZeland is selected to semi")

if NZ_vs_agf=="NZwon" and pak_vs_afg=="afgwon" and pak_vs_NZ=="pakwon":
    print("NewZeland is selected to semi")

if NZ_vs_agf=="NZwon" and pak_vs_afg=="afgwon" and pak_vs_NZ=="NZwon":
    print("NewZeland is selected to semi")

if NZ_vs_agf=="afgwon" and pak_vs_afg=="afgwon" and pak_vs_NZ=="NZwon":
    if NZ_net_rate>afg_net_rate:
        print("NewZeland is selected to semi")
    else:
        print("Afanisthan is selected to semi")



if pak_vs_NZ=="NZwon"  or  NZ_vs_agf=="NZwon"  :
    print("NewZeland is selected to semi")
else:
    print("NewZeland is not selected to semi")




