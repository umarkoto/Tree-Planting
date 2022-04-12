# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class TanamPohon(models.Model):
    _name = 'um.treeplanting'
    _description = 'Tree Planting'
    _inherit = ['mail.thread']

    name = fields.Char(string='Referens', readonly=True, default='/')
    nama_penanam = fields.Many2one('res.partner', string="Nama", default=lambda self: self.env.user.partner_id)
    # entitas = fields.Char('Entitas', default=lambda self: self.env.user.entitas)
    nrp = fields.Char('NRP', default=lambda self: self.env.user.nrp)
    entit = fields.Char('Entitas', default=lambda self: self.env.user.entitas)
    entitas = fields.Many2one('target.pohon')
    # target = fields.Char(string='Target')
    # jenis_pohon = fields.Char(string='Jenis Pohon', required='1')
    # start_date = fields.Date(string='Tanggal Penanaman', required='1')
    # jumlah = fields.Integer(string='Jumlah Ditanam', help='Jumlah yang ditanam hari ini', default=1)
    # image = fields.Binary(string='Foto', help='Cukup 1 foto saja zoom out dari jarak jauh dari pohon yang ditanam')
    # entitas_id = fields.Many2one('tree.entitas', string='Entitas', ondelete='cascade')
    noted = fields.Text(string='Keterangan')
    # lokasi = fields.Char(string='Lokasi', required='1')
    # tree_line = fields.One2many('tanam.pohon', 'tree_id', string='Jumlah Penanam', required=True)
    # update_line = fields.One2many('update.pohon', 'update_id', string='Sesi')


    # target_line = fields.One2many('target.pohon', 'entitas', string='Target')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('um.treeplanting')
        return super(TanamPohon, self).create(vals)


class PenanamPohon(models.Model):
    _name = 'tanam.pohon'
    _description = 'Tanam Pohon'
    # _inherits = {'um.treeplanting': 'entitas'}
    _inherit = ['mail.thread']

    # tree_id = fields.Many2one('um.treeplanting', string='Ref', required=True, ondelete='cascade')
    nama = fields.Many2one('res.users', string="Penanggung Jawab", tracking=True, default=lambda self: self.env.user.id)
    # nama = fields.Many2one('res.partner', string="Nama", default=lambda self: self.env.user.partner_id)
    # nama = fields.Many2one('res.users', string='Penanggung Jawab', default=lambda self: self.env.user.partner_id)
    nrp = fields.Char('NRP', default=lambda self: self.env.user.nrp)
    entit = fields.Char('Entitas', default=lambda self: self.env.user.entitas)
    nama_penanam = fields.Char(string='Nama Penanam', default=lambda self: self.env.user.name)
    jenis_pohon = fields.Char(string='Jenis Pohon', required='1')
    start_date = fields.Date(string='Tanggal Penanaman', required='1')
    jumlah = fields.Integer(string='Jumlah Ditanam', help='Jumlah yang ditanam hari ini', default=1)
    image = fields.Binary(string='Foto', help='Cukup 1 foto saja zoom out dari jarak jauh dari pohon yang ditanam')
    ukuran = fields.Char(string='Ukuran Pohon')
    lokasi = fields.Char(string='Lokasi', required='1')
    relasi = fields.Selection([('suamiistri', 'Suami/Istri'), ('anak', 'Anak'), ('kakak', 'Kakak'), ('adik', 'Adik')],
                               string='Hubungan', default='suamiistri')
    is_employee = fields.Boolean(string='Karyawan', default=True)
    noted = fields.Text(string='Keterangan')

    update_line = fields.One2many('update.pohon', 'update_line_id', string='Update', required=True)
    # active = fields.Boolean(string='Is Employee', default='False')
    # nama_line = fields.One2many('update.pohon', 'nama', string='Sesi')


class TreePlanting(models.Model):
    _name = 'tree.entitas'
    _description = 'Penanaman Pohon'

    name = fields.Many2one('res.partner', string='Entitas')
    ref = fields.Char(string='Referensi', readonly=True, default='/')
    # tree_line = fields.One2many('um.treeplanting', 'entitas_id', string='Jumlah yang ditanam')


class UpdatePohon(models.Model):
    _name = 'update.pohon'
    _description = 'Update Pohon'
    _inherit = ['mail.thread']

    update_line_id = fields.Many2one('tanam.pohon', string='Ref', required=True, ondelete='cascade')
    # nama = fields.Many2one('tanam.pohon', string='Nama Penanam', required=True, ondelete='cascade')
    # update_id = fields.Many2one('um.treeplanting', string='Referens', required=True, ondelete='cascade', default=lambda self: self.env['um.treeplanting'].search([]))
    tanggal_update = fields.Date(string='Tanggal Update')
    image = fields.Binary(string='Foto', help='Cukup 1 foto saja zoom out dari jarak jauh dari pohon yang ditanam')
    ukuran = fields.Char(string='Ukuran Pohon')


class TargetPohon(models.Model):
    _name = 'target.pohon'
    _description = 'Target'

    name = fields.Many2one('res.partner', string='Entitas')
    target = fields.Integer(string='Target')
    active = fields.Boolean(string='Is Active', default='True')
