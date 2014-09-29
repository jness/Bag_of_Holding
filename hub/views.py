from django.shortcuts import render, redirect
from hub.models import Icon, Item, Character, Slot
from hub.forms import ItemUpdateForm, ItemForm
from django.template.defaultfilters import slugify
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'hub/home.html', dict())


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')

    charas = Character.objects.filter(owner=request.user)
    return render(request, 'hub/profile.html', dict(characters=charas))


def create_character(request):
    if not request.user.is_authenticated:
        return redirect('/profile')

    if request.method == 'POST':
        name = request.POST['name']
        chara = Character.objects.create(name=name, owner=request.user)
        Slot.objects.create(name="%s's Inventory" % chara.name, character=chara)

    return redirect('/profile')


def create_slot(request, character_id):
    if not request.user.is_authenticated:
        return redirect('/')

    chara = Character.objects.get(id=character_id)
    if not request.user == chara.owner:
        raise Exception('You do not have access to add slots for this username.')

    if request.method == 'POST':
        name = request.POST['name']
        Slot.objects.create(name=name, character=chara)

    return redirect('/character/%s/' % chara.id)


def delete_slot(request, character_id, slot_id):
    if not request.user.is_authenticated:
        return redirect('/')

    chara = Character.objects.get(id=character_id)
    if not request.user == chara.owner:
        raise Exception('You do not have access to add slots for this username.')

    slot = Slot.objects.get(id=slot_id)
    if not chara == slot.character:
        raise Exception('You do not have access to add slots for this username.')

    slot.delete()

    return redirect('/character/%s/' % chara.id)


def rename_slot(request, character_id, slot_id):
    if not request.user.is_authenticated:
        return redirect('/')

    chara = Character.objects.get(id=character_id)
    if not request.user == chara.owner:
        raise Exception('You do not have access to this character.')

    slot = Slot.objects.get(id=slot_id)
    if not chara == slot.character:
        raise Exception('You do not have access to add slots for this username.')

    if request.method == 'POST':
        name = request.POST['name']
        slot.name = name
        slot.save()

    return redirect('/character/%s/' % chara.id)


def character(request, character_id):
    chara = Character.objects.get(id=character_id)
    slots = Slot.objects.filter(character=chara).order_by('name')
    items = Item.objects.filter(character=chara).order_by('name')

    # Determine if this object should be readonly.
    readonly = True
    if request.user == chara.owner:
        readonly = False

    icons = Icon.objects.all().order_by('image')
    return render(request, 'hub/character.html', dict(
        icons=icons, character=chara, slots=slots, items=items,
        readonly=readonly))


def create_item(request, character_id):
    chara = Character.objects.get(id=character_id)
    if not request.user == chara.owner:
        raise Exception('You do not have access to add items for this username.')

    slots = Slot.objects.filter(character=chara)
    icons = Icon.objects.all().order_by('image')
    return render(request, 'hub/create.html', dict(
        icons=icons, character=chara, slots=slots))


def update_item(request, character_id, item_id):
    chara = Character.objects.get(id=character_id)
    if not request.user == chara.owner:
        raise Exception('You do not have access to add items for this username.')

    item = Item.objects.get(id=item_id)
    if not chara == item.character:
        raise Exception('This item does not belong to you.')

    slots = Slot.objects.filter(character=chara)
    icons = Icon.objects.all().order_by('image')
    return render(request, 'hub/update.html', dict(
        icons=icons, character=chara, slots=slots, item=item))


def add(request, character_id):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        chara = Character.objects.get(id=character_id)
        if not request.user == chara.owner:
            raise Exception('You do not have access to add items for this username.')

        form = ItemForm(request.POST)
        if form.is_valid():

            slot = Slot.objects.get(id=request.POST['slot'])
            if not chara == slot.character:
                raise Exception('You do not have access to add items to this slot.')

            name = request.POST['name']
            link = request.POST['link']
            description = request.POST['description']
            quantity = request.POST['quantity']

            icon = Icon.objects.get(id=request.POST['icon'])
            item = Item.objects.create(name=name, description=description,
                                       quantity=quantity, icon=icon,
                                       character=chara, slot=slot, link=link)

            return redirect('/character/%s#%s' % (
                character_id, slugify(item.name)))
        else:
            raise Exception('Form not valid..')


def update(request, character_id, item_id):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        chara = Character.objects.get(id=character_id)
        if not request.user == chara.owner:
            raise Exception('You do not have access to add items for this username.')

        item = Item.objects.get(id=item_id)

        form = ItemUpdateForm(request.POST)
        if form.is_valid():

            slot = Slot.objects.get(id=request.POST['slot'])
            if not chara == slot.character:
                raise Exception('You do not have access to add items to this slot.')

            name = request.POST['name']
            link = request.POST['link']
            description = request.POST['description']
            quantity = request.POST['quantity']
            icon = Icon.objects.get(id=request.POST['icon'])

            item.name = name
            item.description = description
            item.quantity = quantity
            item.icon = icon
            item.slot = slot
            item.link = link
            item.save()

            return redirect('/character/%s#%s' % (
                character_id, slugify(item.name)))
        else:
            raise Exception('Form not valid..')


def trash(request, character_id, item_id):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        chara = Character.objects.get(id=character_id)
        if not request.user == chara.owner:
            raise Exception('You do not have access to add items for this username.')

        item = Item.objects.get(id=item_id)
        if not item.character == chara:
            raise Exception('You do not have access to this item.')

        item = Item.objects.get(id=item_id)
        item.delete()
        item.save()

    return redirect('/character/%s' % character_id)


def mylogin(request):
    if not request.user.is_authenticated:
        return redirect('/profile/')

    data = dict()
    if request.method == 'POST':
        auth_form = AuthenticationForm(None, request.POST or None)
        if auth_form.is_valid():
            login(request, auth_form.get_user())
            return redirect('/profile/')
        else:
            data['error'] = 'Incorrect username or password.'

    return render(request, 'hub/login.html', data)


def mylogout(request):
    logout(request)
    return redirect('/')


def update_password(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        user = request.user
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            user.set_password(password)
            user.save()
            return redirect('/profile/')
        else:
            return render(request, 'hub/change_password.html',
                          dict(error='Passwords do not match'))

    return render(request, 'hub/change_password.html', dict())