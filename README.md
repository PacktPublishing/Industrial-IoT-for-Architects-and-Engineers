# Industrial IoT for Architects and Engineers

<a href="https://www.packtpub.com/product/industrial-iot-for-architects-and-engineers/9781803240893?utm_source=github&utm_medium=repository&utm_campaign=9781803240893"><img src="https://static.packt-cdn.com/products/9781803240893/cover/smaller" alt="" height="256px" align="right"></a>

This is the code repository for [Industrial IoT for Architects and Engineers](https://www.packtpub.com/product/industrial-iot-for-architects-and-engineers/9781803240893?utm_source=github&utm_medium=repository&utm_campaign=9781803240893), published by Packt.

**Architecting secure, robust, and scalable industrial IoT solutions with AWS**

****

## What is this book about?
When it comes to using the core and managed services available on AWS for making decisions about architectural environments for an enterprise, there are as many challenges as there are advantages. This Industrial IoT book follows the journey of data from the shop floor to the boardroom, identifying goals and aiding in strong architectural decision-making. 

This book covers the following exciting features:
* Discover Industrial IoT best practices and conventions
* Understand how to get started with edge computing
* Define and build IoT solution architectures from scratch
* Use AWS as the core of your solution platform
* Apply advanced analytics and machine learning to your data
* Deploy edge processing to react in near real time to events within your environment

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/180324089X) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, chapter04.

The code will look like the following:
```
def lambda_handler(event, context):
    
    print("Received event: " + json.dumps(event, indent=2))
```

**Following is what you need for this book:**
This book is for architects, engineers, developers, and technical professionals interested in building an edge and cloud-based Internet of Things ecosystem with a focus on industry solutions. Since the focus of this book is specifically on IoT, a solid understanding of core IoT technologies and how they work is necessary to get started. If you are someone with no hands-on experience, but are familiar with the subject, you’ll find the use cases useful to learn how architectural decisions are made.

With the following software and hardware list you can run all code files present in the book (Chapter 1-8).
### Software and Hardware List
 | <b>Soft ware/hardware covered in the book</b> | <b>Operating system requirements</b> |
 | ------------------------------------ | ----------------------------------- |
 | <b>Python</b>: Knowledge of Python will be helpful. Code examples are in Python but are easy to follow if you are unfamiliar with the language. The code samples are easy to read and edit in your environment. | Much of the hands-on work is done within the AWS console. You will require an AWS account and some familiarity. Most examples work within the free tier; however, in the final chapter, which uses Amazon SageMaker, you should track your cost closely. |
 | <b>Visual Studio Code</b>: This is used in some of the later chapters for all the Python code examples. This includes lambdas and edge components that we create. As an IDE, it is easy to use and free! | All the edge processing examples within the book use the Linux operating system, which may require knowing the basic commands when working on a Linux system. |
 |  <b>Edge device</b>: An edge device for installing and running Greengrass will be necessary. A Raspberry Pi will do the trick if you can find one. It should be on the same network as your Modbus simulator or device. This simulator can be a Windows edge device or PC if you are more comfortable with that OS. |  |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/wi9wN).

### Related products
* Industrial Digital Transformation [[Packt]](https://www.packtpub.com/product/industrial-digital-transformation/9781800207677?utm_source=github&utm_medium=repository&utm_campaign=9781800207677) [[Amazon]](https://www.amazon.com/dp/1800207670)

* Building Industrial Digital Twins [[Packt]](https://www.packtpub.com/product/building-industrial-digital-twins/9781839219078?utm_source=github&utm_medium=repository&utm_campaign=9781839219078) [[Amazon]](https://www.amazon.com/dp/1839219076)

## Get to Know the Authors
**Joey Bernal**<br>
Anthony (Joey) Bernal is a creative technical leader focused on the Internet of Things (IoT) and cloud architecture. He has led the development of two major commercial IoT platforms from conception to general availability. He built and ran an IoT start-up, recognized by both Fast Company and Gartner, with customers in manufacturing, oil and gas, and agriculture. Joey is a hands-on architect with solid experience in development, infrastructure, IoT hardware, and cloud and edge platforms. He is an experienced writer and presenter with leadership skills, flexibility, creativity, and technical know-how, which have led to the delivery of many successful products and projects and a sense of humor to enjoy still doing it.

**Bharath Sridhar**<br>
Bharath Sridhar is a technology evangelist and solution architect with over 12 years of experience in digital transformation through IoT. With a constantly curious and exploratory mindset, he works as an enabler of industry 4.0 implementations for Fortune 500 companies. He loves to operate at the intersection of desirability, viability, and feasibility, working to create utilitarian solutions that people love and businesses get delighted and technologists get excited about. He is passionate about knowledge sharing through storytelling. He believes that books are a gateway to curated journeys of personal discovery, experiences, and enlightened knowledge. In his free time, he dreams about the multiverse – its evolution, challenges, and solutions.
