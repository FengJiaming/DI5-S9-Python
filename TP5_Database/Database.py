import sqlite3
import xml.etree.ElementTree as ET


class Database(object):

    def __init__(self):
        self.conn = sqlite3.connect('database/organisation_fr.db')
        self.cursor = self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.close()

    # Créer une table des communes et insérer des données
    def extractCommunes(self, filename):
        # Create table.
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS communes(
                     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                     code_region INTEGER,
                     nom_region VARCHAR,
                     code_departement VARCHAR,
                     code_arrondissement INTEGER,
                     code_canton INTEGER,
                     code_commune INTEGER,
                     nom_commune VARCHAR,
                     population_municipale INTEGER,
                     population_compteeAPart INTEGER,
                     population_totale INTEGER
                )
                """)
        self.conn.commit()

        # Lisez CSV et insérez des données dans la base de données.
        with open(filename, 'rb') as file:
            for commune in file.readlines():
                commune = commune.decode("Windows-1252")
                commune = commune.split(";")
                try:
                    if (int(commune[0]) >= 0 and int(commune[0]) <= 99):
                        for i in [2, 3, 4, 5, 7, 8, 9]:
                            if " " in commune[i]:
                                commune[i] = commune[i].replace(' ', '')
                        data = {
                            "code_region": int(commune[0]),
                            "nom_region": commune[1],
                            "code_departement": commune[2],
                            "code_arrondissement": int(commune[3]),
                            "code_canton": int(commune[4]),
                            "code_commune": int(commune[5]),
                            "nom_commune": commune[6],
                            "population_municipale": int(commune[7]),
                            "population_compteeAPart": int(commune[8]),
                            "population_totale": int(commune[9])
                        }
                        self.cursor.execute("""
                                INSERT INTO communes(   code_region,
                                                        nom_region,
                                                        code_departement,
                                                        code_arrondissement,
                                                        code_canton,
                                                        code_commune,
                                                        nom_commune,
                                                        population_municipale,
                                                        population_compteeAPart,
                                                        population_totale)
                                VALUES( :code_region,
                                        :nom_region,
                                        :code_departement,
                                        :code_arrondissement,
                                        :code_canton,
                                        :code_commune,
                                        :nom_commune,
                                        :population_municipale,
                                        :population_compteeAPart,
                                        :population_totale)
                                """, data)
                except Exception as exception_retournee:
                    pass
        self.conn.commit()

    def extractDepartements(self, filename):
        # Créer une table des departements et insérer des données
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS departements(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             code_region INTEGER,
             nom_region VARCHAR,
             code_departement VARCHAR,
             nom_departement VARCHAR,
             nb_arrondissements INTEGER,
             nb_cantons INTEGER,
             nb_communes INTEGER,
             population_municipale INTEGER,
             population_totale INTEGER
        )
        """)
        self.conn.commit()

        # Lisez CSV et insérez des données dans la base de données.
        with open(filename, 'rb') as file:
            for departement in file.readlines():
                departement = departement.decode("Windows-1252")
                departement = departement.split(";")
                try:
                    if (int(departement[0]) >= 0 and int(departement[0]) <= 99):
                        for i in [0, 4, 5, 6, 7, 8, 9]:
                            if " " in departement[i]:
                                departement[i] = departement[i].replace(' ', '')
                        data = {
                            "code_region": int(departement[0]),
                            "nom_region": departement[1],
                            "code_departement": departement[2],
                            "nom_departement": departement[3],
                            "nb_arrondissements": int(departement[4]),
                            "nb_cantons": int(departement[5]),
                            "nb_communes": int(departement[6]),
                            "population_municipale": int(departement[7]),
                            "population_totale": int(departement[8]),
                        }
                        self.cursor.execute("""
                        INSERT INTO departements(   code_region,
                                                    nom_region,
                                                    code_departement,
                                                    nom_departement,
                                                    nb_arrondissements,
                                                    nb_cantons,
                                                    nb_communes,
                                                    population_municipale,
                                                    population_totale)
                        VALUES( :code_region,
                                :nom_region,
                                :code_departement,
                                :nom_departement,
                                :nb_arrondissements,
                                :nb_cantons,
                                :nb_communes,
                                :population_municipale,
                                :population_totale)
                        """, data)
                except Exception as exception_retournee:
                    pass
        self.conn.commit()

    def extractRegions(self, filename):
        # Créer une table des regions et insérer des données
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS regions(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             code_region INTEGER,
             nom_region VARCHAR,
             nb_arrondissements INTEGER,
             nb_cantons INTEGER,
             nb_communes INTEGER,
             population_municipale INTEGER,
             population_totale INTEGER
        )
        """)

        self.conn.commit()

        # Lisez CSV et insérez des données dans la base de données.
        with open(filename, 'rb') as file:
            for region in file.readlines():
                region = region.decode("Windows-1252")
                region = region.split(";")
                try:
                    if (int(region[0]) >= 0 and int(region[0]) <= 99):
                        for i in [0, 2, 3, 4, 5, 6]:
                            if " " in region[i]:
                                region[i] = region[i].replace(' ', '')
                        data = {
                            "code_region": int(region[0]),
                            "nom_region": region[1],
                            "nb_arrondissements": int(region[2]),
                            "nb_cantons": int(region[3]),
                            "nb_communes": int(region[4]),
                            "population_municipale": int(region[5]),
                            "population_totale": int(region[6])
                        }
                        self.cursor.execute("""
                        INSERT INTO regions (   code_region,
                                                nom_region,
                                                nb_arrondissements,
                                                nb_cantons,
                                                nb_communes,
                                                population_municipale,
                                                population_totale)
                        VALUES( :code_region,
                                :nom_region,
                                :nb_arrondissements,
                                :nb_cantons,
                                :nb_communes,
                                :population_municipale,
                                :population_totale)
                        """, data)
                except Exception as exception_retournee:
                    pass
        self.conn.commit()

    # Afficher les populations totales de chaque département et région
    def computePopulation(self):
        self.cursor.execute("""SELECT nom_departement, population_totale FROM departements""")
        for departement in self.cursor.fetchall():
            print("Département \"" + departement[0] + "\": " + str(departement[1]))

        self.cursor.execute("""SELECT nom_region, population_totale FROM regions""")
        for region in self.cursor.fetchall():
            print("Région \"" + region[0] + "\": " + str(region[1]))

    # Pour déterminer les communes ayant le même nom et un département différent
    def findDifferent(self):
        self.cursor.execute("""
                            SELECT communes.nom_commune, GROUP_CONCAT(departements.code_departement)
                            FROM communes
                            INNER JOIN departements ON communes.code_departement = departements.code_departement
                            GROUP BY communes.nom_commune
                            HAVING COUNT(*) > 1
                            ORDER BY COUNT(*)
                            """)
        for doublon in self.cursor.fetchall():
            print("Commune \"" + doublon[0] + "\": " + doublon[1])

    def saveXML(self, filename):
        with open(filename, "w", encoding="UTF-8") as outfile:#encoding="UTF-8" encoding="Windows-1252"
            self.cursor.execute("""SELECT * FROM regions""")
            rows_regions = self.cursor.fetchall()
            outfile.write('<?xml version="1.0" ?>\n')
            outfile.write('<mydata>\n')
            for row in rows_regions:
                outfile.write('  <row>\n')
                outfile.write('    <code_region>%s</code_region>\n' % row[0])
                outfile.write('    <nom_region>%s</nom_region>\n' % row[1])
                outfile.write('    <nb_arrondissements>%s</nb_arrondissements>\n' % row[2])
                outfile.write('    <nb_cantons>%s</nb_cantons>\n' % row[3])
                outfile.write('    <nb_communes>%s</nb_communes>\n' % row[4])
                outfile.write('    <population_municpale>%s</population_municpale>\n' % row[5])
                outfile.write('    <population_totale>%s</population_totale>\n' % row[6])
                outfile.write('  </row>\n')
            outfile.write('</mydata>\n')

    def chargeXML(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        try:
            for child in root:
                print(child.find('code_region').text)
                data = {
                    "code_region": int(child.find('code_region').text),
                    "nom_region": child.find('nom_region').text,
                    "nb_arrondissements": child.find('nb_arrondissements').text,
                    "nb_cantons": int(child.find('nb_cantons').text),
                    "nb_communes": int(child.find('nb_communes').text),
                    "population_municipale": int(child.find('population_municpale').text),
                    "population_totale": int(child.find('population_totale').text)
                }
                print(data)
                self.cursor.execute("""
                                        INSERT INTO regions (   code_region,
                                                                nom_region,
                                                                nb_arrondissements,
                                                                nb_cantons,
                                                                nb_communes,
                                                                population_municipale,
                                                                population_totale)
                                        VALUES( :code_region,
                                                :nom_region,
                                                :nb_arrondissements,
                                                :nb_cantons,
                                                :nb_communes,
                                                :population_municipale,
                                                :population_totale)
                                        """, data)
        except Exception as exception_retournee:
            print(exception_retournee)
        self.conn.commit()

    def newRegion(self, filename1, filename2):
        self.cursor.execute('''CREATE TABLE if not exists nouvellesRegions
                     (code_nouv_reg integer, libelle_geographique text)''')

        file = open(filename1, "rt", encoding="Windows-1252")
        file_content = file.read()
        file_content = file_content.split("\n")

        # Récupère uniquement les lignes REG du fichier
        for line in file_content:
            if len(line) > 0:
                data_array = line.split(";")
                if len(data_array[0]) > 0:
                    if data_array[0].__eq__('REG'):
                        self.cursor.execute("INSERT INTO nouvellesRegions values (?, ?)", (data_array[1], data_array[2]))
        file.close()

        self.cursor.execute('ALTER TABLE departements ADD COLUMN code_nouv_reg interger')

        file = open(filename2, "rt", encoding="Windows-1252")
        file_content = file.read()
        file_content = file_content.split("\n")

        del file_content[0:7]

        departements_updated = []
        for line in file_content:
            if len(line) > 0:
                data_array = line.split(";")
                if len(data_array[0]) > 0:
                    if not data_array[2] in departements_updated:
                        self.cursor.execute('update departements set code_nouv_reg = ' + data_array[3] + ' where code_departement = \'' +
                                  data_array[2] + '\'')
                        departements_updated.append(data_array[2])
        file.close()
        self.conn.commit()

    def computeNewPopulation(self):
        self.cursor.execute('SELECT nouvellesRegions.code_nouv_reg, libelle_geographique, SUM(communes.population_totale) FROM nouvellesRegions '
                  'INNER JOIN departements on departements.code_nouv_reg = nouvellesRegions.code_nouv_reg '
                  'INNER JOIN communes on communes.code_departement = departements.code_departement GROUP BY nouvellesRegions.code_nouv_reg')
        for row in self.cursor:
            print("Nouvelle région code: " + str(row[0]) + " Nom: \"" + row[1] + "\": " + str(row[2]))

    # Effacer la base de données
    def reset(self):
        self.cursor.execute('''DROP TABLE IF EXISTS regions''')
        self.cursor.execute('''DROP TABLE IF EXISTS departements''')
        self.cursor.execute('''DROP TABLE IF EXISTS communes''')
        self.cursor.execute('''DROP TABLE IF EXISTS nouvellesRegions''')
        self.conn.commit()
