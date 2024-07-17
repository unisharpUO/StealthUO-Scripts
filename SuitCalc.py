from py_stealth import *


if __name__ == '__main__':
    AddToSystemJournal('Starting script')

    hci = dci = ssi = di = lmc = fc = fcr = cf = sdi = dex = stren = intel\
        = hp = stam = mana = manaRegen = 0
    hpRegen = stamRegen = lrc = 0

    #  dci += 5
    #  hci += 5
    #  di += 5
    #  stren += 5

    for _i in range(1, 29):
        if 'hide' in GetTooltip(ObjAtLayer(_i)).split("|")[0] or \
                'studded' in GetTooltip(ObjAtLayer(_i)).split("|")[0] or \
                'bone' in GetTooltip(ObjAtLayer(_i)).split("|")[0]:
            lmc += 3
        for _p in GetTooltipRec(ObjAtLayer(_i)):
            if _p['Cliloc_ID'] == 1060415:  # hci
                hci += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060408:  # dci
                dci += int(_p['Params'][0])
                print(f'{GetTooltip(ObjAtLayer(_i))}')
            elif _p['Cliloc_ID'] == 1060486:  # ssi
                ssi += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060402:  # di
                di += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060433:  # lmc
                lmc += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060434:  # lrc
                lrc += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060413:  # fc
                fc += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060412:  # fcr
                fcr += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1113696:  # cf
                cf += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060483:  # sd
                sdi += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060409:  # dex
                dex += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060485:  # stren
                stren += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060432:  # intel
                intel += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060431:  # hp
                hp += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060484:  # stam
                stam += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060439:  # mana
                mana += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060440:  # manaRegen
                manaRegen += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060444:  # hpRegen
                hpRegen += int(_p['Params'][0])
            elif _p['Cliloc_ID'] == 1060443:  # stamRegen
                stamRegen += int(_p['Params'][0])

    print(f'hci: {hci}, dci: {dci}, ssi: {ssi}, di: {di}')
    print(f'lrc: {lrc}, lmc: {lmc}, fc: {fc}, fcr: {fcr}, cf: {cf}, sd: {sdi}')
    print(f'stren: {stren}, dex: {dex}, intel: {intel}')
    print(f'hp: {hp}, stam: {stam}, mana: {mana}')
    print(f'hpRegen: {hpRegen}, manaRegen: {manaRegen}, stamRegen: {stamRegen}')
    totalstat = stren + dex + intel + hp + stam + mana
    print(f'total stat:{totalstat}')

    exit()
