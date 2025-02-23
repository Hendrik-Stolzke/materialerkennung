from mldog.app.context import DefaultDrillContext
from mldog.app.plugins.liveMaterialRecognition.liveMaterialRecognition import LiveMaterialRecognition
from mldog.app.plugins.liveThreeMaterialRecognition.liveThreeMaterialRecognition import LiveThreeMaterialRecognition
from mldog.app.ui.ui import MLDOGUI



if __name__ == '__main__':
    # construct a new application context instance
    context = DefaultDrillContext()

    # register additional application plugins
    # context.registerApplication(<your-application-class-here>, 'Your Application Name/Title Here')

    context.registerApplication(LiveMaterialRecognition, 'LiveMaterialRecognition')
    context.registerApplication(LiveThreeMaterialRecognition, 'LiveMaterialRecognition for 3 Materials')
    
    # run GUI for context
    ui = MLDOGUI(context)
    ui.run()
