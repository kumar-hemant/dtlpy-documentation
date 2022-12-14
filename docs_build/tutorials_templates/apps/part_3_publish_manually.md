# Part 3: Publish the App to the Platform 

In order to install an application to your project, you must use the python SDK or the CLI, whichever you prefer.

But first, we need to publish the app to the platform:

```shell
dpl app publish --project-name <PROJECT_NAME>
```

Now we can install the app in any project

CLI
```shell
dlp app install --project-name <PROJECT_NAME>
```

Through the SDK - run the following commands

```
import dtlpy
project = dtlpy.projects.get(project_name='name', project_id='id')
installed_app = project.apps.install(dpk_id='dpk_id')
 ```

Note: Currently, When you install an application through either of these ways, you won’t be able to set the settings of the application.

 

 

Typical Workflow:

Create an application (the FE and BE)

Initialize the application using the command line/python SDK (and maybe a template in the future)

Test your application locally, with the debugging tool in the platform

Tweak in the process the app.json file to accommodate your needs.

Build your application and move the files into the appropriate panel directory. (NOTE: the application entry point is the index.html file)

CURRENTLY: add the directory to the path of the generated js/CSS files

Deploy your application. (You might need to change the env using dl.setenv() for Dataloop developers)

Sample script: (Run it in the root folder of your application)


project = dl.projects.get(project_id='<ID>')
dpk = project.dpks.publish()
Install your application using the dpk store in OA, with the appropriate settings

in the frame - right click -> View Frame Source -> `this is unsafe` and reload the frame

 

Changing the application configuration to build in the right directory:

Vue - change ‘vue.config.js’ outputDir property to the directory of the panel

React - and .env file to the root folder of your project, and add BUILD_PATH='PATH_TO_PANEL'

Angular - open the angular.json file and change projects.<APP_NAME>.architect.build.options.outputPath to the path of the panel.

 

