# -*- coding: utf-8 -*-


def grid():
    if not auth.user:
        redirect(URL('default', 'index'))
    grid = SQLFORM.grid(db.bread)
    return dict(grid=grid)

def new():
    form = SQLFORM(db.bread)
    if form.process().accepted:
        response.flash = 'Pan enviado'
        session.has_sent_bread = True
    return dict(form=form)

def view():
    if not session.bads:
        session.bads = {}
    button_active = True
    if request.post_vars.get('id', False):
        bread_id = int(request.post_vars.get('id'))
        db(db.bread.id == bread_id).update(bad=db.bread.bad + 1)
        session.bads[bread_id] = True

    bread_id = request.args(0, cast=int)
    if bread_id in session.bads:
        button_active = False
    return dict(bread=db.bread(bread_id), button_active=button_active)