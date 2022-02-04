class User:
  def __init__(self, name, password_hash, model_access):
    self.name = name
    self.password_hash = password_hash
    self.model_access = model_access