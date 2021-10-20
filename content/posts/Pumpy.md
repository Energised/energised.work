Title: Pumpy - The Open Source Medical Syringe Pump
Date: 2020-06-10 17:18
Modified: 2020-06-10 17:19
Category: 3D Printing
Tags: electronics, rpi, python
Slug: pumpy-syringe-pump
Authors: Dan Woolsey
Summary: Open-Source solution to expensive medical devices

## Abstract

Due to COVID-19, medical equipment and PPE have been in short supply and high demand. For the first time,
hospitals relied on individuals to 3D print face masks to handle the growing supply concerns they faced.
This has the potential to be applied to other forms of medical equipment such as syringe pumps, which provide
continuous, hands-free drug delivery and can cost more than £1500 per unit.

In this project we designed, 3D printed and built 2 medical-use syringe pumps based on Joshua Pearce's Open
Source Syringe Pump. We programmed both a touchscreen interface for a Raspberry Pi computer and an Android
application for remote pump operation via Bluetooth.

We have demonstrated that medical-use syringe pumps can be built for less than 10% of their market value. This
open-source approach to manufacturing equipment can allow hospitals to handle supply issues internally and can
help to provide inexpensive medical equipment to poor areas with limited modern technology.

## Pumpy

![pump v2 pic](/images/pump-v2-pic.png)

The Pumpy Syringe Pump is based on the Open Source Syringe Pump Library by Joshua Pearce et al [1]. Several modifications to
the electronics systems and the structure of hte pump were made using Open Source resources online along with my
own knowledge of electronics. The aim is to provide the information and designs for users to build their
own pumps that are heavily customisable for any number of use cases. Other syringe pump projects have worked
to produce Pumps for specific use cases, mostly in chemical and scientific research areas.

For my dissertation I wanted to show that low cost and independently manufactured medical equipment is possible
in an age where it's now easy for consumers to design and manufacture plastic components for all sorts of 
purposes.



## References

[1]("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0107216")
