print("Welcome to Dhruv's Physics Calculator")
calc=str(input('Enter the calculation(no capital letters): '))

if(calc=='velocity'):
    displacement=float(input('Enter the displacement:'))
    time=float(input('Enter the time:'))
    velocity=displacement/time
    print('%0.3f is the output velocity.' %(velocity))
elif(calc=='acceleration'):
    velocity2=float(input('Enter the velocity:'))
    time2=float(input('Enter the time:'))
    acceleration=velocity2/(time2)*(time2)
    print('%0.3f is the output acceleration.' %(acceleration))
elif(calc=='force'):
    mass=float(input('Enter the mass:'))
    acceleration2=float(input('Enter the acceleration:'))
    force=mass*acceleration2
    print('%0.3f is the output force.' %(force))
elif(calc=='weight'):
    mass2=float(input('Enter the mass:'))
    gravity=9.8
    weight=mass*gravity
    print('%0.3f is the weight.' %(weight))
elif(calc=='work'):
    force2=float(input('Enter the force:'))
    distance=float(input('Enter the distance:'))
    work=force2*distance
    print('%0.3f is the work.' %(work))
elif(calc=='power'):
    work2=float(input('Enter the work:'))
    time3=float(input('Enter the time:'))
    power=work2/time3
    print('%0.3f is the power.' %(power))
elif(calc=='momentum'):
    mass3=float(input('Enter the mass:'))
    velocity3=float(input('Enter the velocity:'))
    momentum=mass3*velocity3
    print('%0.3f is the momentum.' %(momentum))
elif(calc=='momentum'):
    mass3=float(input('Enter the mass:'))
    velocity3=float(input('Enter the velocity:'))
    momentum=mass3*velocity3
    print('%0.3f is the momentum.' %(momentum))
elif(calc=='energy'):
    mass4=float(input('Enter the mass:'))
    lightspeed=299,792,458
    energy=mass*lightspeed*lightspeed
    print('%0.3f is the energy' %(energy))
elif(calc=='potentialenergy'):
    mass5=float(input('Enter the mass:'))
    height=float(input('Enter the height:'))
    penergy=mass5*height*gravity
    print('%0.3f is the potentional energy' %(penergy))
elif(calc=='kineticenergy'):
    mass6=float(input('Enter the mass:'))
    velocity4=float(input('Enter the velocity:'))
    kenergy=(mass6*velocity4*velocity4)/2
    print('%0.3f is the kinetic energy' %(kenergy))
elif(calc=='pressure'):
    force3=float(input('Enter the force:'))
    area=float(input('Enter the area:'))
    pressure=force3/area
    print('%0.3f is the pressure' %(pressure))
elif(calc=='density'):
    mass7=float(input('Enter the mass:'))
    volume=float(input('Enter the volume:'))
    density=mass7/volume
    print('%0.3f is the density' %(density))
elif(calc=='charge'):
    current=float(input('Enter the current:'))
    time4=float(input('Enter the time:'))
    charge=current*time4
    print('%0.3f is the charge' %(charge))
elif(calc=='potentialdifference'):
    current2=float(input('Enter the current:'))
    resistance=float(input('Enter the resistance:'))
    potentialdifference=current2*resistance
    print('%0.3f is the potentialdifference' %(potentialdifference))
elif(calc=='power2'):
    potentialdifference2=float(input('Enter the potential difference:'))
    current3=float(input('Enter the current:'))
    power2=current3*potentialdifference2
    print('%0.3f is the power' %(power2))
elif(calc=='frequency'):
    period=float(input('Enter the period:'))
    frequency=1/period
    print('%0.3f is the frequency' %(frequency))
elif(calc=='capicitance'):
    chargestore=float(input('Enter the charge stored:'))
    potentialdifference3=float(input('Enter the potential difference:'))
    capicitance=chargestore/potentialdifference3
    print('%0.3f is the capicitance' %(capicitance))
elif(calc=='wavespeed'):
    frequency2=float(input('Enter the frequency:'))
    wavelength=float(input('Enter the potential difference:'))
    wavespeed=wavelength*frequency2
    print('%0.3f is the wave speed' %(wavespeed))
elif(calc=='displacement'):
    finaldisplacement=float(input('Enter the final displacement:'))
    regulardisplacement=float(input('Enter the initial displacement:'))
    displacement2=finaldisplacement-regulardisplacement
    print('%0.3f is the displacement' %(displacement2))
elif(calc=='Intensity'):
    area2=float(input('Enter the area:'))
    power3=float(input('Enter the power:'))
    intensity=power3/area2
    print('%0.3f is the intensity' %(intensity))
elif(calc=='current4'):
    charge2=float(input('Enter the charge:'))
    time5=float(input('Enter the time:'))
    current4=charge2/time5
    print('%0.3f is the current' %(current4))
elif(calc=='current5'):
    voltage=float(input('Enter the voltage:'))
    resistance2=float(input('Enter the resistance:'))
    current5=voltage/resistance
    print('%0.3f is the current' %(current5))
elif(calc=='avlife'):
    wavelength2=float(input('Enter the wavelength:'))
    avlife=1/wavelength2
    print('%0.3f is the wavelength' %(wavelength2))
elif(calc=='cost'):
    amount=float(input('Enter the amount:'))
    price=float(input('Enter the price:'))
    cost=amount*price
    print('%0.3f is the cost' %(cost))
elif(calc=='mass8'):
    force4=float(input('Enter the force:'))
    acceleration3=float(input('Enter the acceleration:'))
    mass8=force4*acceleration3
    print('%0.3f is the mass' %(mass))
elif(calc=='finalvelocity'):
    initialvelocity=float(input('Enter the initial velocity:'))
    acceleration4=float(input('Enter the acceleration:'))
    time6=float(input('Enter the acceleration:'))
    finalvelocity=initialvelocity+acceleration4*time6
    print('%0.3f is the final velocity' %(finalvelocity))
elif(calc=='finalvelocity2'):
    initialvelocity2=float(input('Enter the initial velocity:'))
    acceleration5=float(input('Enter the acceleration:'))
    time7=float(input('Enter the acceleration:'))
    displacement3=float(input('Enter the displacement:'))
    finalvelocity*finalvelocity=initialvelocity*initialvelocity+acceleration5*time7*displacement3
    print('%0.3f is the final velocity' %(finalvelocity2))
elif(calc=='flowRate'):
    volume2=float(input('Enter the amount:'))
    time8=float(input('Enter the price:'))
    flowRate=volume2/time8
    print('%0.3f is the flow rate' %(flowRate))
elif(calc=='massFlow'):
    mass9=float(input('Enter the amount:'))
    time9=float(input('Enter the time:'))
    massFlow=mass9/time9
    print('%0.3f is the mass flow rate' %(massFlow))
