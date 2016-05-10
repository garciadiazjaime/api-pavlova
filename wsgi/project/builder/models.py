from __future__ import unicode_literals

from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    order = models.IntegerField(null=True, blank=True, default=0)

    def __unicode__(self):
        return "%s" % (self.name)

class Block(models.Model):
    name = models.CharField(max_length=150)
    order = models.IntegerField(null=True, blank=True, default=0)
    section = models.ForeignKey(Section)

    def __unicode__(self):
        return "%s - %s" % (self.id, self.name)

class Slide(models.Model):
    image = models.CharField(max_length=500)
    title = models.CharField(max_length=150, null=True, blank=True)
    button_title = models.CharField(max_length=150, null=True, blank=True)
    button_url = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    block = models.ForeignKey(Block, related_name='slides')

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "%s" % (self.title)

class Title(models.Model):
    content = models.CharField(max_length=500)
    block = models.ForeignKey(Block, related_name='titles')

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "%s" % (self.content)

class Paragraph(models.Model):
    content = models.TextField()
    block = models.ForeignKey(Block, related_name='paragraphs')

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "%s" % (self.content)

class Image(models.Model):
    src = models.CharField(max_length=500)
    alt = models.CharField(max_length=150)
    block = models.ForeignKey(Block, related_name='images')

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "%s" % (self.src)

class Button(models.Model):
    href = models.CharField(max_length=500)
    title = models.CharField(max_length=150)
    block = models.ForeignKey(Block, related_name='buttons')

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "%s" % (self.href)
