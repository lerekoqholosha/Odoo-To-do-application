#-*- coding: utf-8 -*-
from odoo import fields,models,api

class Todo_Task(models.Model):
      _name='todo.task'
      _description='to-do task'

      name=fields.Char('Title',required=True)
      description=fields.Text('description',required=True)
      date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now())
      is_done=fields.Boolean('Done?')
      active=fields.Boolean('Active?',default=True)

      @api.multi
      def do_toggle_done(self):
          for task in self:
              task.is_done = not task.is_done
          return True

      @api.model
      def do_clear_done(self):
          dones = self.search([('is_done', '=', True)])
          dones.write({'active': False})
          return True