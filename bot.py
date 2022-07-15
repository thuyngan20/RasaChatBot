from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/MyNLU')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhooks/slack/webhook")

agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput(slack_token="xoxp-3791814281347-3788964565781-3788459649559-e1a8a6eb3b08b5a4cf295c0780cc06a2")

agent.handle_channels([input_channel], 5002, serve_forever=True)


