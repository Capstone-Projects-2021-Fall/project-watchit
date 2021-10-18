const Joi = require("joi");

// Schema for registration. Fields should conform to these restrictions.
const registerSchema = Joi.object({
  //username: Joi.string().min(4).max(30).alphanum().required(),
  username: Joi.string().min(4).max(30).required(),
  password: Joi.string().required().min(8).max(30),
  confirmPassword: Joi.any()
    .equal(Joi.ref("password"))
    .required()
    .label("Confirm password")
    .options({ messages: { "any.only": "{{#label}} does not match" } }),
});

// Function that validates registration using Joi.validate
const registrationValidation = (data) => {
  return registerSchema.validate(data);
};

// Schema for login
const loginSchema = Joi.object({
  username: Joi.string().required(),
  password: Joi.string().required(),
});

// Function that validates login
const loginValidation = (data) => {
  return loginSchema.validate(data);
};

module.exports = {
  registrationValidation: registrationValidation,
  loginValidation: loginValidation,
};
