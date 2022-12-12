# Part 2: Run The App Locally


install dependencies
run using cli
make code change
run unittest


####################
Create a debug application:

Before deploying your application, you want to test it in a fast manner. For that reason, we have the debug application feature, which allows you to run your application locally and test it on the run on the platform, and see the changes immediately as they happen,

 

Before deploying your application, you want to test it in a fast manner. For that reason, we have the debug application feature, which allows you to run your application locally and test it on the run on the platform, and see the changes immediately as they happen,

 

Create the FE and BE for the application in a framework of your choice

Note: If you are using plain html without running in on a specific port, you will need to install the npm package http-server (via the command `npm i -g http-server`), and run `http-server`. Sometimes you’ll also need to enable cors by adding the `–cors` option.

Create an app.json file to your root location (there is no validation about the JSON file, it doesn’t affect the operation of the application, currently).

Example of basic dapp.json:


{

  "components": {

    "panels": [

      {

        "name": "preview-modality",

        "minRole": "annotator",

        "supportedSlots": [

          {

            "type": "itemSidePanel",

            "configuration": {

              "route": []

            }

          }

        ],

        "conditions": {

          "resources": []

        },

        "icon": "icon-dl-sdk-documentation",

        "metadata": {},

        "defaultSettings": {

        }

      }

    ]

  }

}
 

Open the platform and navigate to Faas -> Application Hub and go to the `Developer` Tab.

Click the Add function button at the top left corner

Name your application, set the address to the appropriate URL, and specify the required slot.


And now you are ready to run your application.

 

Using dlapplib.js in your application:

When using the platform, it’s most likely that you will interact with the platform’s entities, such as item, project, organization, etc… For that, we have created the js SDK to use in your app.

 

Add to your index.html file the script:

<script src="https://local.dataloop.ai:8443/dlAppLib.js"></script>

And use the dl module in your application

When using a framework: You must access it through the `window` object (i.e. window.dl), if you going to use it in conjunction with Typescript, you should add // @ts-ignore before every use so it won’t complain that this property doesn’t exist

 

OR

 

Add the following lines to the main.ts file

 

declare global {

    interface Window {

        dl: any

        XFrameManager: any

        GuestAgent: any

    }

}

Add dl.init()

Wait until it completed initialization, your can listen to that using dl.on(‘ready’, () => {})

And you are ready to go, you can use the SDK just like the python SDK, with the advantage of not needing to set the item id/name when you are in the item viewer, or the project when getting it.

 



