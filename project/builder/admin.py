from django.contrib import admin
import nested_admin

from .models import Section, Block, Slide, Title, Paragraph, Image, Button


# Register your models here.
class ChoiceSlide(admin.StackedInline):
	model = Slide
	extra = 1

class ChoiceTitle(admin.StackedInline):
	model = Title
	extra = 1

class ChoiceParagraph(admin.StackedInline):
	model = Paragraph
	extra = 1

class ChoiceImage(admin.StackedInline):
	model = Image
	extra = 1

class ChoiceButton(admin.StackedInline):
	model = Button
	extra = 1

class ChoiceBlock(nested_admin.NestedStackedInline):
    model = Block
    extra = 1
    inlines = [ChoiceSlide, ChoiceTitle, ChoiceParagraph, ChoiceImage, ChoiceButton]

class SectionAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'name', 'slug', 'order')
    inlines = [ChoiceBlock,]


admin.site.register(Section, SectionAdmin)
