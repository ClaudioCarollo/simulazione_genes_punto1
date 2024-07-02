from database.DB_connect import DBConnect
from model.conneesione import Connessione
from model.gene import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
                    from genes g
                    where g.Essential ='Essential' 
                    group by g.GeneID
                    order by g.GeneID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idmap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g1.GeneID as gene1, g2.GeneID as gene2, i.Expression_Corr as espressione
                from genes g1, genes g2, interactions i  
                where g1.GeneID = i.GeneID1 
                and g2.GeneID = i.GeneID2
                and g1.Essential = 'Essential'
                and g2.Essential = 'Essential' 
                and g1.GeneID != g2.GeneID
                group by g1.GeneID, g2.GeneID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idmap[row["gene1"]], idmap[row["gene2"]], row["espressione"]))

        cursor.close()
        conn.close()
        return result


