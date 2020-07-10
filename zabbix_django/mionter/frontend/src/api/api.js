import axiosServer from './axios'


export const loginSubmit = (data) => axiosServer.post(`/login`, data)

export const getHostApp = (hostId) => axiosServer.get(`v1/host/${hostId}/application`)
export const DeleteHostApp = (hostId, data) => axiosServer.delete(`v1/host/${hostId}/application`, data)
export const PutHostApp = (hostId, data) => axiosServer.put(`v1/host/${hostId}/application`, data)
export const AddHostApp = (hostId, data) => axiosServer.post(`v1/host/${hostId}/application`, data)


export const getItem = (hostId, applyId) => axiosServer.get(`v1/host/${hostId}/application/${applyId}/item`)
export const DeleteItem = (hostId, applyId, data) => axiosServer.delete(`v1/host/${hostId}/application/${applyId}/item`, data)
export const PutItem = (hostId, applyId, data) => axiosServer.put(`v1/host/${hostId}/application/${applyId}/item`, data)
export const AddItem = (hostId, applyId, data) => axiosServer.post(`v1/host/${hostId}/application/${applyId}/item`, data)

export const getHost = () => axiosServer.get(`/v1/host`)
export const DeleteHost = (data) => axiosServer.delete(`/v1/host`, data)
export const PutHost = (data) => axiosServer.put(`/v1/host`, data)
export const AddHost = (data) => axiosServer.post(`/v1/host`, data)

export const getHostgroup = () => axiosServer.get(`/v1/hostgroup`)
export const DeleteHostgroup = (data) => axiosServer.delete(`/v1/hostgroup`, data)
export const PutHostgroup = (data) => axiosServer.put(`/v1/hostgroup`, data)
export const AddHostgroup = (data) => axiosServer.post(`/v1/hostgroup`, data)

export const getTemplate = () => axiosServer.get(`v1/template`)
export const getTemplateApplication = (template_id) => axiosServer.get(`v1/template/${template_id}/application`)
export const getTemplateItem = (template_id, application_id) => axiosServer.get(`v1/template/${template_id}/application/${application_id}/item`)

export const getTrigger = (hostId) => axiosServer.get(`v1/host/${hostId}/trigger`)
export const AddTrigger = (hostId, data) => axiosServer.get(`v1/host/${hostId}/trigger`, data)
export const PutTrigger = (hostId, data) => axiosServer.get(`v1/host/${hostId}/trigger`, data)
export const DeleteTrigger = (hostId, data) => axiosServer.get(`v1/host/${hostId}/trigger`, data)

export const getKey = () => axiosServer.get(`v1/itemkey`)