"""
@author: koka
"""
import init
import button_text_start_finish as btsf
   
# отлов ивентов и нажатий
init.root.bind('<Left>', btsf.moveLeft)
init.root.bind('<Right>', btsf.moveRight)
init.root.bind('<Up>', btsf.moveUp)
init.root.bind('<Down>', btsf.moveDown)
init.root.bind('<space>', btsf.change)

# основной цыкл (последняя строчка)
init.root.mainloop()