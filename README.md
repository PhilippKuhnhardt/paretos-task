# How to run

1. Install venv: `py -3 -m venv venv`
2. Activate venv: `venv\Scripts\activate`

This was programmed on python 3.10.2. Be sure to check that your interpreter and the version in venv/pyvenv.cfg is 3.10.2, or it may not work properly.

3. Install Flask: `pip install Flask`
4. Install Flask-HTTPAuth: `pip install Flask-HTTPAuth`
5. Run: `flask run`


# How to use

- To use a model, send a POST request to: `http://127.0.0.1:5000/models/<modelId>`
- The body needs to contain a JSON object with the required input parameters, e.g.:
```
{
	"number1": 4,
	"number2": 3,
	"number3": 3
}
```
- You need to authenticate yourself via Basic Auth to use a model
- You can use GET `http://127.0.0.1:5000/models` to check what models you have access to with your user


# Available users:

```
User: Philipp
Password: password
Available Models: multiplicationModel, sumModel
```

```
User: Éric
Password: strong_password
Available Models: divisionModel
```

# Models:

```
ModelId: multiplicationModel
Inputs: "number1", "number2"
Outputs: The numbers multiplicated
```

```
ModelId: sumModel
Inputs: "number1", "number2", "number2"
Outputs: The numbers summed up
```

```
ModelId: divisionModel
Inputs: "number1", "number2"
Outputs: The numbers divided
```

# What needs to be improved:

This is obviously not even close to finished. There are several issues that would need to be tackled before it could be considered "finished":
- It's not very dynamic, you can't just add a model and be done with it, you need to hardcode it into the code
- -> Ideally I just want to add a .py-file for a model and register it in another file
- You can't create / update users, users and hashed pws aren't stored in a db, you can't assign models to users dynamically
- Lack of testing
- The API doesn't give you good feedback why it doesn't work
