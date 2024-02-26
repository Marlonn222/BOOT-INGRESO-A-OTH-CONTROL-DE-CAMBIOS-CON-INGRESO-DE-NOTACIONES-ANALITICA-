import time
import pyautogui
from time import sleep
import pyperclip
import pendulum
from storagefunctions import (pressingKey,selectToEnd,formatDate)

def searchOTHControl(incidentId, cheklist):
    
    crm_dashboard = crm_assign_user = OTH_Control_Cambio = crm_edit_tarea = crm_assign_user = crm_save_OTH = crm_otp_saved_sucessfully = crm_warning_message = crm_ot_blocked_message = mod_consulta_popup = None 
    crmAttempts = 0
    
    #/////////////////////////////////// CRM DASHBOARD ///////////////////////////////////////////    
    
    while crm_dashboard is None:
        crm_dashboard = pyautogui.locateOnScreen('C:/OTHSoporte/assets/crm_dashboard.png', grayscale = True,confidence=0.85)
        sleep(0.5)
        if crmAttempts == 5:
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].minimize()
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].maximize()
            print("Estoy dentro de los 5 intentos para ver el Dashboard del CRM")
            crmAttempts = 0
        crmAttempts = crmAttempts + 1
                
    print("CRM Dashboard GUI is present!")   
    pyautogui.click(pyautogui.center(crm_dashboard))    
    
    sleep(0.5)
    pressingKey('f2')
    while mod_consulta_popup is None:        
        mod_consulta_popup = pyautogui.locateOnScreen('C:/OTHSoporte/assets/mod_consulta_popup.png', grayscale = True,confidence=0.85)            
        pressingKey('f2')
    print("mod_consulta_popup field is present and detected on GUI screen!")
    sleep(0.5)
    pyautogui.write(incidentId)
    sleep(0.5)
    pressingKey('enter')
    
    #/////////////////////////////////// FASE DE INGRESO ///////////////////////////////////////////
    
    while crm_ot_blocked_message is None and crm_warning_message is None and crmAttempts < 10:
        crm_warning_message = pyautogui.locateOnScreen('C:/OTHSoporte/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_ot_blocked_message = pyautogui.locateOnScreen('C:/OTHSoporte/assets/crm_ot_blocked_message.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        if crmAttempts == 8:
            print("Estoy dentro de los 8 intentos de medio seg para esperar algun pop up de OT bloqueada inesperado en el CRM")                        
        crmAttempts += 1
        print(crmAttempts)            
            
    # Maximize CRM window 
    pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].maximize()
    print("CRM view Window was maximized!")    
    
    #//////////////////////////////////// INGRESE A LA OTH //////////////////////////////////
    time.sleep(1)
    pyautogui.doubleClick(1218,469) 
    crmAttempts = 0
    time.sleep(1)
    pyautogui.click(681,519)
    time.sleep(1)
    
    while OTH_Control_Cambio is None:
        print("buscando OTH_Control_Cambio in screen")
        OTH_Control_Cambio = pyautogui.locateOnScreen('C:/OTHSoporte/assets/OTH_Control_Cambio.png', grayscale = True,confidence=0.95)                                
    print("OTH_Control_Cambio is present!")
    pyautogui.moveTo(pyautogui.center(OTH_Control_Cambio))            
    pyautogui.doubleClick()
    sleep(1)

    # Maximize CRM OTH window 
    pyautogui.getWindowsWithTitle("Tarea hija")[0].maximize()
    print("CRM OTH Edit view Window was maximized!")            
            
    # Validate edit_incident view is visible and on focus  edita la tarea          
    while crm_edit_tarea is None:
        crm_edit_tarea = pyautogui.locateOnScreen('C:/OTHSoporte/assets/edit_tarea.png', grayscale = True,confidence=0.9)   
    print("Vista de Detalles is present!")    
    print("CRM OTH Edit tarea button is present!")
    crm_edit_tarea_x,crm_edit_tarea_y = pyautogui.center(crm_edit_tarea)
    pyautogui.click(crm_edit_tarea_x, crm_edit_tarea_y)    
    
    # Validate assign user pop up is visible and on focus
    # crm_assign_user = None  # reset variable   
    crmAttempts = 0
    while crm_assign_user is None and crmAttempts < 5:
        crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        print("buscando ventana de asignación de usuario")
        crmAttempts +=1      

    if crm_assign_user is not None:
        print("CRM OTH Confirm Assign Pop Up is present!")
        sleep(1)
        pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
        sleep(1)
    
    #/////////////////////////////////// TRASLADO DE COMENTARIOS /////////////////////////////////////    
    pressingKey('tab')
    sleep(1)
    pyperclip.copy(cheklist)
    sleep(0.5)
    pyautogui.hotkey('ctrl','v')    
    sleep(0.5)  

    #/////////////////////////////////// GUARDADO COMENTARIOS /////////////////////////////////////    
    while crm_save_OTH is None:
        crm_save_OTH = pyautogui.locateOnScreen('C:/OTHSoporte/assets/guardar_tarea_button.png', grayscale = True,confidence=0.9)   
    print("CRM OTH Save Incident button is present!")
    crm_save_OTH_x,crm_save_OTH_y = pyautogui.center(crm_save_OTH)
    pyautogui.click(crm_save_OTH_x, crm_save_OTH_y)   
    
    sleep(1)    
    crm_assign_user = None
    while crm_warning_message is None and crm_assign_user is None:  
        print("buscando o crm_warning_message o crm_assign_user")      
        crm_warning_message = pyautogui.locateOnScreen('C:/OTHSoporte/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
        sleep(0.5)                
        
    if(crm_warning_message is None):
        print("CRM empty_warning_message_crm pop up is not present!")
                
        # Validate assign user pop up is visible and on focus   
        crm_assign_user = None  # reset variable
        crmAttempts = 0
        while crm_assign_user is None and crmAttempts < 5:
            crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
            sleep(0.5)
            print("buscando ventana de asignación de usuario")            
            crmAttempts +=1            
        if crm_assign_user is not None:
            print("CRM Confirm Assign Pop Up is present!")
            sleep(1)
            pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
            sleep(1)

        # Validate save OTP successfully  pop up is visible and on focus   
        while crm_otp_saved_sucessfully is None:
            crm_otp_saved_sucessfully = pyautogui.locateOnScreen('C:/OTHSoporte/assets/OTH_guardado_exitosamente.png', grayscale = True,confidence=0.9)   
        print("CRM OTP Saved Succesfully Pop Up is present!")
        sleep(1)
        pressingKey('enter')
        sleep(1)

        # Cierre ventana OTH
        pyautogui.getWindowsWithTitle("Tarea hija")[0].close()        
        sleep(1.5)
        # Validate if changes must be saved or not and Close the OT Details View On Edition mode  
        # Close Edit Incident View 
        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1.5)
        return 0
    else:
        print("CRM empty_warning_message_crm pop up is present!")
        #pyautogui.click(pyautogui.center(crm_warning_message))
        sleep(0.5)
        pressingKey('enter')
        sleep(1)
        pressingKey('enter')
        sleep(1)
        pyautogui.getWindowsWithTitle("Tarea hija")[0].close()  
        sleep(1)  
        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1)
        pressingKey('n')        
            
        return 9
        
        # Validate assign user pop up is visible and on focus   
        crm_assign_user = None  # reset variable
        crmAttempts = 0
        while crm_assign_user is None and crmAttempts < 5:
            crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_operador.png', grayscale = True,confidence=0.9)   
            sleep(0.5)
            print("buscando ventana de asignación de usuario")
            crmAttempts +=1            
        if crm_assign_user is not None:
            print("CRM Confirm Assign Pop Up is present!")
            sleep(1)
            pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
            sleep(1)

        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1.5)
        
        # You must Validate assign user pop up is visible and on focus
        sleep(1)
        pressingKey('n') # No re asignar usuario al momento de editar las OTPs         
        print("n key has been pressed!")         
def searchOTHControlLimitante(incidentId, anotaciones, anotaciones1, anotaciones2, anotaciones3, anotaciones4):
    
    crm_dashboard = crm_assign_user = OTH_Control_Cambio = crm_edit_tarea = crm_assign_user = crm_save_OTH = crm_otp_saved_sucessfully = crm_warning_message = crm_ot_blocked_message = mod_consulta_popup = None 
    crmAttempts = 0
    
    #/////////////////////////////////// CRM DASHBOARD ///////////////////////////////////////////    
    
    while crm_dashboard is None:
        crm_dashboard = pyautogui.locateOnScreen('C:/OTHSoporte/assets/crm_dashboard.png', grayscale = True,confidence=0.85)
        sleep(0.5)
        if crmAttempts == 5:
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].minimize()
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].maximize()
            print("Estoy dentro de los 5 intentos para ver el Dashboard del CRM")
            crmAttempts = 0
        crmAttempts = crmAttempts + 1
                
    print("CRM Dashboard GUI is present!")   
    pyautogui.click(pyautogui.center(crm_dashboard))    
    
    sleep(0.5)
    pressingKey('f2')
    while mod_consulta_popup is None:        
        mod_consulta_popup = pyautogui.locateOnScreen('C:/OTHSoporte/assets/mod_consulta_popup.png', grayscale = True,confidence=0.85)            
        pressingKey('f2')
    print("mod_consulta_popup field is present and detected on GUI screen!")
    sleep(0.5)
    pyautogui.write(incidentId)
    sleep(0.5)
    pressingKey('enter')
    
    #/////////////////////////////////// FASE DE INGRESO ///////////////////////////////////////////
    
    while crm_ot_blocked_message is None and crm_warning_message is None and crmAttempts < 10:
        crm_warning_message = pyautogui.locateOnScreen('C:/OTHSoporte/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_ot_blocked_message = pyautogui.locateOnScreen('C:/OTHSoporte/assets/crm_ot_blocked_message.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        if crmAttempts == 8:
            print("Estoy dentro de los 8 intentos de medio seg para esperar algun pop up de OT bloqueada inesperado en el CRM")                        
        crmAttempts += 1
        print(crmAttempts)            
            
    # Maximize CRM window 
    pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].maximize()
    print("CRM view Window was maximized!")    
    
    #//////////////////////////////////// INGRESE A LA OTH //////////////////////////////////
    time.sleep(1)
    pyautogui.doubleClick(1218,469) 
    crmAttempts = 0
    time.sleep(1)
    pyautogui.click(681,519)
    time.sleep(1)
    
    while OTH_Control_Cambio is None:
        print("buscando OTH_Control_Cambio in screen")
        OTH_Control_Cambio = pyautogui.locateOnScreen('C:/OTHSoporte/assets/OTH_Control_Cambio.png', grayscale = True,confidence=0.95)                                
    print("OTH_Control_Cambio is present!")
    pyautogui.moveTo(pyautogui.center(OTH_Control_Cambio))            
    pyautogui.doubleClick()
    sleep(1)

    # Maximize CRM OTH window 
    pyautogui.getWindowsWithTitle("Tarea hija")[0].maximize()
    print("CRM OTH Edit view Window was maximized!")            
            
    # Validate edit_incident view is visible and on focus  edita la tarea          
    while crm_edit_tarea is None:
        crm_edit_tarea = pyautogui.locateOnScreen('C:/OTHSoporte/assets/edit_tarea.png', grayscale = True,confidence=0.9)   
    print("Vista de Detalles is present!")    
    print("CRM OTH Edit tarea button is present!")
    crm_edit_tarea_x,crm_edit_tarea_y = pyautogui.center(crm_edit_tarea)
    pyautogui.click(crm_edit_tarea_x, crm_edit_tarea_y)    
    
    # Validate assign user pop up is visible and on focus
    # crm_assign_user = None  # reset variable   
    crmAttempts = 0
    while crm_assign_user is None and crmAttempts < 5:
        crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        print("buscando ventana de asignación de usuario")
        crmAttempts +=1      

    if crm_assign_user is not None:
        print("CRM OTH Confirm Assign Pop Up is present!")
        sleep(1)
        pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
        sleep(1)
    
    #/////////////////////////////////// TRASLADO DE COMENTARIOS /////////////////////////////////////    
    pressingKey('tab')
    sleep(1)
    # rango de limitacion para la fecha
    fecha_inicio = pendulum.parse('12/01/2023', strict=False)
    fecha_fin = pendulum.parse('12/12/2024', strict=False)
    
    # Columna OBSERVACIONES_KO OBSERVACION 1
    # Anotaciones contiene el texto con la fecha al inicio
    if ':' in anotaciones:
        parts = anotaciones.split(':', 1)  # Dividir el texto en dos partes usando ':' como separador
        fecha_texto = parts[0].strip()  # Obtener la parte que contiene la fecha
        texto_despues_fecha = parts[1].strip()  # Obtener el texto después de la fecha

        try:
            fecha = pendulum.parse(fecha_texto, strict=False)

            # Verificar si la fecha está dentro del rango deseado
            if fecha_inicio <= fecha <= fecha_fin:
                pyperclip.copy("OBSERVACIONES_KO: ")  
                pyautogui.hotkey('ctrl','v') 
                sleep(0.5)
                #pyperclip.copy(fecha)
                #pyautogui.hotkey('ctrl','v')    
                pyperclip.copy(texto_despues_fecha)
                pyautogui.hotkey('ctrl','v')
                sleep(0.5)    
                pyautogui.press('enter')
            else:
                print("Fecha fuera del rango:")

        except ValueError:
            print("Formato de fecha incorrecto en:", fecha_texto)
    
    # Columna ESTADO UM OBSERVACION 2
    # Anotaciones contiene el texto con la fecha al inicio
    if ':' in anotaciones1:
        parts1 = anotaciones1.split(':', 1)  # Dividir el texto en dos partes usando ':' como separador
        fecha_texto1 = parts1[0].strip()  # Obtener la parte que contiene la fecha
        texto_despues_fecha1 = parts1[1].strip()  # Obtener el texto después de la fecha

        try:
            fecha1 = pendulum.parse(fecha_texto1, strict=False)

            # Verificar si la fecha está dentro del rango deseado
            if fecha_inicio <= fecha1 <= fecha_fin:
                pyperclip.copy("OBSERVACIONES_UM: ")  
                pyautogui.hotkey('ctrl','v') 
                sleep(0.5)
                #pyperclip.copy(fecha)
                #pyautogui.hotkey('ctrl','v')    
                pyperclip.copy(texto_despues_fecha1)
                pyautogui.hotkey('ctrl','v')
                sleep(0.5)    
                pyautogui.press('enter')
            else:
                print("Fecha fuera del rango:")

        except ValueError:
            print("Formato de fecha incorrecto en:", fecha_texto1)
    
    # Columna OBSERVACIONES_CONFIG OBSERVACION 3
    # Anotaciones contiene el texto con la fecha al inicio
    if ':' in anotaciones2:
        parts2 = anotaciones2.split(':', 1)  # Dividir el texto en dos partes usando ':' como separador
        fecha_texto2 = parts2[0].strip()  # Obtener la parte que contiene la fecha
        texto_despues_fecha2 = parts2[1].strip()  # Obtener el texto después de la fecha

        try:
            fecha2 = pendulum.parse(fecha_texto2, strict=False)

            # Verificar si la fecha está dentro del rango deseado
            if fecha_inicio <= fecha2 <= fecha_fin:
                pyperclip.copy("OBSERVACIONES_CONFIG: ")  
                pyautogui.hotkey('ctrl','v') 
                sleep(0.5)
                #pyperclip.copy(fecha)
                #pyautogui.hotkey('ctrl','v')    
                pyperclip.copy(texto_despues_fecha2)
                pyautogui.hotkey('ctrl','v')
                sleep(0.5)    
                pyautogui.press('enter')
            else:
                print("Fecha fuera del rango:")

        except ValueError:
            print("Formato de fecha incorrecto en:", fecha_texto2)

    # Columna OBSERVACIONES_EQUI OBSERVACION 4
    # Anotaciones contiene el texto con la fecha al inicio
    if ':' in anotaciones3:
        parts3 = anotaciones3.split(':', 1)  # Dividir el texto en dos partes usando ':' como separador
        fecha_texto3 = parts3[0].strip()  # Obtener la parte que contiene la fecha
        texto_despues_fecha3 = parts3[1].strip()  # Obtener el texto después de la fecha

        try:
            fecha3 = pendulum.parse(fecha_texto3, strict=False)

            # Verificar si la fecha está dentro del rango deseado
            if fecha_inicio <= fecha3 <= fecha_fin:
                pyperclip.copy("OBSERVACIONES_EQUI: ")  
                pyautogui.hotkey('ctrl','v') 
                sleep(0.5)
                #pyperclip.copy(fecha)
                #pyautogui.hotkey('ctrl','v')    
                pyperclip.copy(texto_despues_fecha3)
                pyautogui.hotkey('ctrl','v')
                sleep(0.5)    
                pyautogui.press('enter')
            else:
                print("Fecha fuera del rango:")

        except ValueError:
            print("Formato de fecha incorrecto en:", fecha_texto3)

    # Columna OBSERVACIONES_EQUI OBSERVACION 5
    # Anotaciones contiene el texto con la fecha al inicio
    if ':' in anotaciones4:
        parts4 = anotaciones4.split(':', 1)  # Dividir el texto en dos partes usando ':' como separador
        fecha_texto4 = parts4[0].strip()  # Obtener la parte que contiene la fecha
        texto_despues_fecha4 = parts4[1].strip()  # Obtener el texto después de la fecha

        try:
            fecha4 = pendulum.parse(fecha_texto4, strict=False)

            # Verificar si la fecha está dentro del rango deseado
            if fecha_inicio <= fecha4 <= fecha_fin:
                pyperclip.copy("OBSERVACIONES_ES: ")  
                pyautogui.hotkey('ctrl','v') 
                sleep(0.5)
                #pyperclip.copy(fecha)
                #pyautogui.hotkey('ctrl','v')    
                pyperclip.copy(texto_despues_fecha4)
                pyautogui.hotkey('ctrl','v')
                sleep(0.5)    
                pyautogui.press('enter')
            else:
                print("Fecha fuera del rango:")

        except ValueError:
            print("Formato de fecha incorrecto en:", fecha_texto4)

    #/////////////////////////////////// GUARDADO COMENTARIOS /////////////////////////////////////    
    while crm_save_OTH is None:
        crm_save_OTH = pyautogui.locateOnScreen('C:/OTHSoporte/assets/guardar_tarea_button.png', grayscale = True,confidence=0.9)   
    print("CRM OTH Save Incident button is present!")
    crm_save_OTH_x,crm_save_OTH_y = pyautogui.center(crm_save_OTH)
    pyautogui.click(crm_save_OTH_x, crm_save_OTH_y)   
    
    sleep(1)    
    crm_assign_user = None
    while crm_warning_message is None and crm_assign_user is None:  
        print("buscando o crm_warning_message o crm_assign_user")      
        crm_warning_message = pyautogui.locateOnScreen('C:/OTHSoporte/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
        sleep(0.5)                
        
    if(crm_warning_message is None):
        print("CRM empty_warning_message_crm pop up is not present!")
                
        # Validate assign user pop up is visible and on focus   
        crm_assign_user = None  # reset variable
        crmAttempts = 0
        while crm_assign_user is None and crmAttempts < 5:
            crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
            sleep(0.5)
            print("buscando ventana de asignación de usuario")            
            crmAttempts +=1            
        if crm_assign_user is not None:
            print("CRM Confirm Assign Pop Up is present!")
            sleep(1)
            pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
            sleep(1)

        # Validate save OTP successfully  pop up is visible and on focus   
        while crm_otp_saved_sucessfully is None:
            crm_otp_saved_sucessfully = pyautogui.locateOnScreen('C:/OTHSoporte/assets/OTH_guardado_exitosamente.png', grayscale = True,confidence=0.9)   
        print("CRM OTP Saved Succesfully Pop Up is present!")
        sleep(1)
        pressingKey('enter')
        sleep(1)

        # Cierre ventana OTH
        pyautogui.getWindowsWithTitle("Tarea hija")[0].close()        
        sleep(1.5)
        # Validate if changes must be saved or not and Close the OT Details View On Edition mode  
        # Close Edit Incident View 
        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1.5)
        return 0
    else:
        print("CRM empty_warning_message_crm pop up is present!")
        #pyautogui.click(pyautogui.center(crm_warning_message))
        sleep(0.5)
        pressingKey('enter')
        sleep(1)
        pressingKey('enter')
        sleep(1)
        pyautogui.getWindowsWithTitle("Tarea hija")[0].close()  
        sleep(1)  
        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1)
        pressingKey('n')        
            
        return 9
        
        # Validate assign user pop up is visible and on focus   
        crm_assign_user = None  # reset variable
        crmAttempts = 0
        while crm_assign_user is None and crmAttempts < 5:
            crm_assign_user = pyautogui.locateOnScreen('C:/OTHSoporte/assets/asignar_ot_usuario_operador.png', grayscale = True,confidence=0.9)   
            sleep(0.5)
            print("buscando ventana de asignación de usuario")
            crmAttempts +=1            
        if crm_assign_user is not None:
            print("CRM Confirm Assign Pop Up is present!")
            sleep(1)
            pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
            sleep(1)

        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1.5)
        
        # You must Validate assign user pop up is visible and on focus
        sleep(1)
        pressingKey('n') # No re asignar usuario al momento de editar las OTPs         
        print("n key has been pressed!")         
