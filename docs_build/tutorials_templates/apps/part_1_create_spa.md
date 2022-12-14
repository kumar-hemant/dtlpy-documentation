# Part 1 - Create SPA (Single Page Application)

## Init a Project

To create a new app, create a new folder 'my-first-app' and run the CLI init command:

```shell
mkdir my-first-app
cd  my-first-app
dlp app init
```

You will be asked a series of question to help you initialize the project and viola! You have a new app!

## Project Arch

The directory structure will contain the 'dataloop.json' app file as well as this directory structure:

├── src  
│ ├── controller  
│ │ ├── **/*.css  
│ ├── views  
│ ├── model  
│ └──index.js  
├── modules  
│ ├── func.py  
│ └──main.py  
├── panels  
│ ├── index.html    
│ └── main.py  
├── artifacts  
│ ├── model.pb  
│ └── model.pth  
├── dataloop.json  
├── README.md  
└── .gitignore

### The Dataloop Package (DPK)

The DPK (dataloop package) is the main entity holding an application.
A DPK holds all the required components of the application, the panels it has, the services it uses, and the source code
of the application.
A DPK is represented by the `dataloop.json` file at the root of the project, which specifies the required components of
the application.

## The JSON Structure

```json
{
    "version": "1.0.0",
    "creator": "rotem@dataloop.ai",
    "name": "Hope",
    "displayName": "Hope",
    "description": "This is a",
    "icon": "",
    "categories": [
        "firstApp",
        "mediaPreview"
    ],
    "source": {
        "type": "git",
        "repo": "https://template",
        "tag": "main"
    },
    "scope": "project",
    "components": {
        "panels": [],
        "hooks": [],
        "modules": [],
        "services": [],
        "triggers": [],
        "pipelines": [],
        "models": [],
        "snapshots": []
    }
}
```

## Components

The components are at the core of an application, they define the behavior of the application and its dependencies.

### Panels:

The Panel represents the view the user is going to see. The panel can be viewed in several places, or slots in dataloop
terms, such as:

Data Browser - which overrides the data browser layout, and inflates it with the new layout, specified by the panel. (
TODO: validate)

Floating Window - This creates a new window on top of the platform, which can be dragged and resized, and shows the
panel.

Item Viewer - Overrides the Item viewer content with a custom-made layout to view an item from the task browser or the
dataset browser.

Item Side Panel - Add a new side panel to the Annotation and Info panels in the item viewer.

A sample panel json:

```json
{
    "name": "mediaPreviewer",
    "minRole": "annotator",
    "supportedSlots": [
        {
            "type": "floatingWindow",
            "configuration": {
                "minHeight": 200,
                "minWidth": 200,
                "resizable": true
            }
        }
    ],
    "icon": "dl.icon",
    "metadata": {},
    "defaultSettings": {
        "system": [
            {
                "": [
                    "item.viewer"
                ],
                "query": {
                    "resource": "item",
                    "filters": {}
                },
                "active": true
            }
        ],
        "app": [
            {
                "mediaType": [
                    "image"
                ]
            }
        ]
    }
}
```

### Toolbar

### Modules

The modules are the modules that are required by the application to work properly. They are the Faas module, for more
information, please refer to the documentation FaaS documentation.

### Services

Services are the carriers of the panels. A service is responsible for running a panel and managing its lifecycle. A Faas
service represents the service, For more information about services, please refer to the documentation (TODO: Add link)

(TODO: When it will be final, add documentation that a default service will be created for every panel unless specified
otherwise)

### Triggers

### Pipelines

### Models

### Artifacts



