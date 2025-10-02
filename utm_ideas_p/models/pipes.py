from odoo import models, fields, api



class Pipes(models.Model):
    _name = 'utm.pipes'
    _description = 'Tabla de mapeo Fuente-Medio'

    # Fuente asociada (Guardada en minúsculas)
    source = fields.Char('Source Name', required=True)

    # Definición de medios booleanos
    organic = fields.Boolean('Organic')
    ppc = fields.Boolean('PPC')
    display = fields.Boolean('Display')
    social = fields.Boolean('Social')
    social_paid = fields.Boolean('Social Paid')
    referral = fields.Boolean('Referral')
    email = fields.Boolean('Email')
    newsletter = fields.Boolean('Newsletter')
    sms = fields.Boolean('SMS')
    push = fields.Boolean('Push')

    # Lista de campos booleanos explícitos para ser usados por list_active_mediums
    MEDIUM_FIELDS = [
        'organic', 'ppc', 'display', 'social',
        'social_paid', 'referral', 'email',
        'newsletter', 'sms', 'push'
    ]

    #METODOS OVERRIDE PARA TENER UNA TABLA FACIL DE GESTIONAR POR EL USUARIO: pipes Y OTRA CON LAS TUPLAS fuente/medio: hide_pipes
    def create(self, data):
        record = super().create(data)
        if record:
            hide_pipes = self.env["utm.hide.pipes"]
            sources = self.env["utm.sources"]
            mediums = self.env["utm.mediums"]

            # Crear la fuente si no existe
            source = sources.search([("name", "=", record.source)], limit=1)
            if not source:
                source = sources.create({"name": record.source})

            for field_name, field_obj in self._fields.items():
                if field_obj.type == "boolean" and record[field_name]:
                    print("creando hidepipies1")
                    source = sources.search([("name", "=", record["source"])], limit=1)
                    print(source)
                    medium = mediums.search([("name", "=", field_name)], limit=1)
                    print(mediums.search([]).mapped("name"))
                    print(field_name)
                    if source and medium:
                        print("creando hidepipies")
                        hide_pipes.create({
                            "source_id": source.id,
                            "medium_id": medium.id,
                        })
            print(sources.search([]))
            print(mediums.search([]))
            print(hide_pipes.search([]))
        return record


    def write(self, vals):
        res = super().write(vals)
        hide_pipes = self.env["utm.hide.pipes"]
        sources = self.env["utm.sources"]
        mediums = self.env["utm.mediums"]

        for record in self:
            for field_name, field_obj in self._fields.items():
                if field_obj.type == "boolean" and record[field_name]:
                    source = sources.search([("name", "=", record["source"])], limit=1)
                    medium = mediums.search([("name", "=", field_name)], limit=1)

                    if source and medium:
                        # Si no existe, lo creamos
                        if not hide_pipes.search([("source_id", "=", source.id), ("medium_id", "=", medium.id)], limit=1):
                            hide_pipes.create({
                                "source_id": source.id,
                                "medium_id": medium.id,
                            })
                else:
                    # Si se desactiva el booleano, eliminamos la relación
                    source = sources.search([("name", "=", record["source"])], limit=1)
                    medium = mediums.search([("name", "=", field_name)], limit=1)

                    if source and medium:
                        hp = hide_pipes.search([("source_id", "=", source.id), ("medium_id", "=", medium.id)])
                        hp.unlink()
        return res
    def unlink(self):
        hide_pipes = self.env["utm.hide.pipes"]
        sources = self.env["utm.sources"]
        mediums = self.env["utm.mediums"]

        for record in self:
            for field_name, field_obj in self._fields.items():
                if field_obj.type == "boolean" and record[field_name]:
                    source = sources.search([("name", "=", record["source"])], limit=1)
                    medium = mediums.search([("name", "=", field_name)], limit=1)

                    if source and medium:
                        hp = hide_pipes.search([("source_id", "=", source.id), ("medium_id", "=", medium.id)])
                        hp.unlink()

        return super().unlink()


