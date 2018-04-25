var eventSchema = mongoose.Schema;

var eventSchemaObj = new eventSchema({
	eventtype: { type: String, required: true, unique: false },
	date: {type:String},
	time: {type:String},
  	userpassword: { type: String, required: true },
    usermail    		: String
});

var statsSchemaObj = new statsSchema({
	username : { type: String, required: true, unique: true },
	totalGames : Number,
	wins : Number,
	losses : Number,
	draws : Number

});

//creating models
var Signup = mongoose.model('User', signupSchemaObj);
var Stats = mongoose.model('userStats', statsSchemaObj);

// establishing connection
// mongoose.connect(process.env.MONGODB_URI, function (error) {
//     if (error) 
//     	{
//     		console.error(error);
//     		console.log("error aa rha hai!!");
//     	}
//     else console.log('mongo connected');
// });
mongoose.connect('mongodb://localhost:27017/test', { useMongoClient: true });