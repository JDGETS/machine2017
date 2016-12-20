; Auto-generated. Do not edit!


(cl:in-package pwm_driver-srv)


;//! \htmlinclude SetDutyCycle-request.msg.html

(cl:defclass <SetDutyCycle-request> (roslisp-msg-protocol:ros-message)
  ((channel
    :reader channel
    :initarg :channel
    :type cl:integer
    :initform 0)
   (value
    :reader value
    :initarg :value
    :type cl:integer
    :initform 0))
)

(cl:defclass SetDutyCycle-request (<SetDutyCycle-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetDutyCycle-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetDutyCycle-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pwm_driver-srv:<SetDutyCycle-request> is deprecated: use pwm_driver-srv:SetDutyCycle-request instead.")))

(cl:ensure-generic-function 'channel-val :lambda-list '(m))
(cl:defmethod channel-val ((m <SetDutyCycle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pwm_driver-srv:channel-val is deprecated.  Use pwm_driver-srv:channel instead.")
  (channel m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <SetDutyCycle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pwm_driver-srv:value-val is deprecated.  Use pwm_driver-srv:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetDutyCycle-request>) ostream)
  "Serializes a message object of type '<SetDutyCycle-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'channel)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'value)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetDutyCycle-request>) istream)
  "Deserializes a message object of type '<SetDutyCycle-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'channel)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'value)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetDutyCycle-request>)))
  "Returns string type for a service object of type '<SetDutyCycle-request>"
  "pwm_driver/SetDutyCycleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetDutyCycle-request)))
  "Returns string type for a service object of type 'SetDutyCycle-request"
  "pwm_driver/SetDutyCycleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetDutyCycle-request>)))
  "Returns md5sum for a message object of type '<SetDutyCycle-request>"
  "1ae5219cd7525faee248995c37ceecae")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetDutyCycle-request)))
  "Returns md5sum for a message object of type 'SetDutyCycle-request"
  "1ae5219cd7525faee248995c37ceecae")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetDutyCycle-request>)))
  "Returns full string definition for message of type '<SetDutyCycle-request>"
  (cl:format cl:nil "byte channel~%byte value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetDutyCycle-request)))
  "Returns full string definition for message of type 'SetDutyCycle-request"
  (cl:format cl:nil "byte channel~%byte value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetDutyCycle-request>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetDutyCycle-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetDutyCycle-request
    (cl:cons ':channel (channel msg))
    (cl:cons ':value (value msg))
))
;//! \htmlinclude SetDutyCycle-response.msg.html

(cl:defclass <SetDutyCycle-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass SetDutyCycle-response (<SetDutyCycle-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetDutyCycle-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetDutyCycle-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pwm_driver-srv:<SetDutyCycle-response> is deprecated: use pwm_driver-srv:SetDutyCycle-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetDutyCycle-response>) ostream)
  "Serializes a message object of type '<SetDutyCycle-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetDutyCycle-response>) istream)
  "Deserializes a message object of type '<SetDutyCycle-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetDutyCycle-response>)))
  "Returns string type for a service object of type '<SetDutyCycle-response>"
  "pwm_driver/SetDutyCycleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetDutyCycle-response)))
  "Returns string type for a service object of type 'SetDutyCycle-response"
  "pwm_driver/SetDutyCycleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetDutyCycle-response>)))
  "Returns md5sum for a message object of type '<SetDutyCycle-response>"
  "1ae5219cd7525faee248995c37ceecae")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetDutyCycle-response)))
  "Returns md5sum for a message object of type 'SetDutyCycle-response"
  "1ae5219cd7525faee248995c37ceecae")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetDutyCycle-response>)))
  "Returns full string definition for message of type '<SetDutyCycle-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetDutyCycle-response)))
  "Returns full string definition for message of type 'SetDutyCycle-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetDutyCycle-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetDutyCycle-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetDutyCycle-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetDutyCycle)))
  'SetDutyCycle-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetDutyCycle)))
  'SetDutyCycle-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetDutyCycle)))
  "Returns string type for a service object of type '<SetDutyCycle>"
  "pwm_driver/SetDutyCycle")