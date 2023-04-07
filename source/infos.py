class DocumentInfos:

    title = u'Problème du sac à dos'
    first_name = 'Robin'
    last_name = 'Gachet'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Février'
    seminary_title = u'Travail Personnel'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/grobinbulle/knapsack_ecrit.git"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()