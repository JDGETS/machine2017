; Auto-generated. Do not edit!


(cl:in-package pin_test-srv)


;//! \htmlinclude LedState-request.msg.html

(cl:defclass <LedState-request> (roslisp-msg-protocol:ros-message)
  ((open
    :reader open
    :initarg :open
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass LedState-request (<LedState-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LedState-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LedState-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pin_test-srv:<LedState-request> is deprecated: use pin_test-srv:LedState-request instead.")))

(cl:ensure-generic-function 'open-val :lambda-list '(m))
(cl:defmethod open-val ((m <LedState-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pin_test-srv:open-val is deprecated.  Use pin_test-srv:open instead.")
  (open m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LedState-request>) ostream)
  "Serializes a message object of type '<LedState-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'open) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LedState-request>) istream)
  "Deserializes a message object of type '<LedState-request>"
    (cl:setf (cl:slot-value msg 'open) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LedState-request>)))
  "Returns string type for a service object of type '<LedState-request>"
  "pin_test/LedStateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LedState-request)))
  "Returns string type for a service object of type 'LedState-request"
  "pin_test/LedStateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LedState-request>)))
  "Returns md5sum for a message object of type '<LedState-request>"
  "b06b243ca7fb95b6d7d5a6ac2b1f7c85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LedState-request)))
  "Returns md5sum for a message object of type 'LedState-request"
  "b06b243ca7fb95b6d7d5a6ac2b1f7c85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LedState-request>)))
  "Returns full string definition for message of type '<LedState-request>"
  (cl:format cl:nil "bool open~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LedState-request)))
  "Returns full string definition for message of type 'LedState-request"
  (cl:format cl:nil "bool open~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LedState-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LedState-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LedState-request
    (cl:cons ':open (open msg))
))
;//! \htmlinclude LedState-response.msg.html

(cl:defclass <LedState-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass LedState-response (<LedState-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LedState-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LedState-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pin_test-srv:<LedState-response> is deprecated: use pin_test-srv:LedState-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LedState-response>) ostream)
  "Serializes a message object of type '<LedState-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LedState-response>) istream)
  "Deserializes a message object of type '<LedState-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LedState-response>)))
  "Returns string type for a service object of type '<LedState-response>"
  "pin_test/LedStateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LedState-response)))
  "Returns string type for a service object of type 'LedState-response"
  "pin_test/LedStateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LedState-response>)))
  "Returns md5sum for a message object of type '<LedState-response>"
  "b06b243ca7fb95b6d7d5a6ac2b1f7c85")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LedState-response)))
  "Returns md5sum for a message object of type 'LedState-response"
  "b06b243ca7fb95b6d7d5a6ac2b1f7c85")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LedState-response>)))
  "Returns full string definition for message of type '<LedState-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LedState-response)))
  "Returns full string definition for message of type 'LedState-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LedState-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LedState-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LedState-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LedState)))
  'LedState-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LedState)))
  'LedState-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LedState)))
  "Returns string type for a service object of type '<LedState>"
  "pin_test/LedState")