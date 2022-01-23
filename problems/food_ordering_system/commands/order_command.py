from commands import command_executor


class OrderCommandExecutor(command_executor.CommandExecutor):

	def __init__(self, order_service):
		self.order_service = order_service

	