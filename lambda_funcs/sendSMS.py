var AWS = require('aws-sdk')
var SNS = new AWS.SNS()



exports.handler = async (event) => {
    var params = {
        PhoneNumber: "+65" + event['number'],
        Message: event['message']
    }
    
    return new Promise(function(resolve, reject) {
        SNS.publish(params, function(err, data) {
            if (err) {
                console.log(err)
                reject(err)
            } else {
                console.log(data)
                resolve(data)
            }
        })
    })
}